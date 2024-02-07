import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from src.entrypoint.main import app
from src.entrypoint.database import Base, get_db



SQLALCHEMY_URL = "sqlite:///test.db"

engine = create_engine(
    SQLALCHEMY_URL,
    connect_args={
        "check_same_thread" : False
    },
)


TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
   


client = TestClient(app)




def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
 

'''
This is a pytest fixture thats sets up a new database session for each test function 
It creates a new test DATABASE before each test and delets it after each test.
'''
@pytest.fixture(scope="function")
def db_session():
    # Creates the test database.
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()  # Creates a new session that is used to interact with the database.
    yield session
    
    session.close()
    clear_mappers()
    Base.metadata.drop_all(bind=engine)
    








def test_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == "Diabolical... . . .  .   .   .   .    .     .      .       .       .         .             .             .              ."


