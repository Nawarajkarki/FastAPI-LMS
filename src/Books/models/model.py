import sqlalchemy as sa
from sqlalchemy.orm import relationship


from src.entrypoint.database import Base




class Book(Base):
    __tablename__ = 'books'
    
    id = sa.Column( sa.Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    title = sa.Column( sa.VARCHAR(255), nullable=False)
    isbn = sa.Column( sa.INTEGER, nullable=False, unique=True)
    published_date = sa.Column( sa.DateTime, server_default=sa.func.now())
    genre = sa.Column( sa.VARCHAR(55))
    
    

class BooksDetail(Base):
    __tablename__ = 'books_detail'
    
    id = sa.Column( sa.Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    book_id = sa.Column( sa.Integer, sa.ForeignKey('books.id'),unique=True, nullable=False)
    num_of_pages = sa.Column( sa.INTEGER, nullable=False)
    publisher = sa.Column( sa.VARCHAR(50), nullable=False)
    language = sa.Column( sa.VARCHAR(10))
    
 

class BorrowedBooks(Base):
    __tablename__ = 'books_borrowed'
    
    id = sa.Column( sa.Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    book_id = sa.Column( sa.Integer, sa.ForeignKey('books.id'),unique=True, nullable=False)
    user_id = sa.Column( sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    borrow_date = sa.Column( sa.DateTime, nullable=False)
    return_date = sa.Column( sa.DateTime)
  



