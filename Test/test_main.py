import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, clear_mappers
from sqlalchemy import MetaData


from src.entrypoint.main import app
from src.entrypoint.database import Base, get_db



SQLALCHEMY_URL = "sqlite:///test.db"

engine = create_engine(
    SQLALCHEMY_URL,
    connect_args={
        "check_same_thread" : False
    },
)


TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
   


client = TestClient(app)

# Base.metadata.create_all(bind=engine)



def override_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
 

'''
This is a pytest fixture thats sets up a new database session for each test function 
It creates a new test DATABASE before each test and delets it after each test.
'''
@pytest.fixture(scope='function')
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestSessionLocal()
    
    
    yield db
    
    Base.metadata.drop_all(bind=engine)
    db.close()





def test_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == "Diabolical... . . .  .   .   .   .    .     .      .       .       .         .             .             .              ."


