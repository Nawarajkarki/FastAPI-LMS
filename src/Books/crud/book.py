from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.Books.models import model
from src.Books.schemas import schemas

class BooksCrud():
    
    def __init__(self, db:Session):
        self.db = db
        
        
    def get_books(self, book_id:int | None = None):
        
        if book_id is None:
            book = self.db.query(model.Book).all()
            return book
        book = self.db.query(model.Book).filter(model.Book.id == book_id).first()
        return book 
    
    
    def get_book_by_isbn(self, isbn:int):
        book = self.db.query(model.Book).filter(model.Book.isbn == isbn).first()
        return book
    
    def create_book(self, book : schemas.BookCreate):
        
        new_book = model.Book(title=book.title, isbn=book.isbn, published_date=book.published_date, genre = book.genre)
        self.db.add(new_book)
        self.db.commit()
        self.db.refresh(new_book)
        
        return new_book
        
        
    def update_book_info(self,book_obj, title=None, genre=None):
        if title is not None:
            book_obj.title = title
        if genre is not None:
            book_obj.genre = genre
        
        self.db.commit()
        self.db.refresh(book_obj)
        
        return book_obj
        
                
    

    def delete_book(self, book_obj ):
        
        self.db.delete(book_obj)
        self.db.commit()
        
        return True
        
