from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os


# Please Update this like with your DB connection details
# And also line [ 63 ] of alembic.ini while you are at this.
SQLALCHEMY_URL = "postgresql://postgres:nope@localhost:5432/LMS"



engine  = create_engine(SQLALCHEMY_URL)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





def test_connection():
    try:
        db = SessionLocal()
        result = db.execute(text("SELECT 1"))
        print(result.scalar())
        db.close()
        print("Connection to DataBase successfull")
    except Exception as e:
        print("DB Connection failed:", e)
        

test_connection()