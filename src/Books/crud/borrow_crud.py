from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy import and_

from src.Books.models import model
from src.Books.schemas import schemas



class BorrowBooks():
    
    def __init__(self, db:Session):
        self.db = db
        
    
    def get_borrowed_books_by_user(self, user_id:int):
        return self.db.query(model.BorrowedBooks).filter(model.BorrowedBooks.user_id == user_id).all()
    
    
    def is_borrowed(self, book_id:int):
        
        # borrowed_book = self.db.query(model.BorrowedBooks).filter(model.BorrowedBooks.book_id == book_id, model.BorrowedBooks.return_date.is_(None)).first
        borrowed_book = self.db.query(model.BorrowedBooks).filter(and_(model.BorrowedBooks.book_id == book_id, model.BorrowedBooks.return_date.is_(None))).first()
        if borrowed_book:
            return True
        return borrowed_book
        
        
        
        
    def borrow_book(self, borrow_info : schemas.BorrowBookCreate):
        
        new_borrow = model.BorrowedBooks(**borrow_info.model_dump())
        
        self.db.add(new_borrow)
        self.db.commit()
        self.db.refresh(new_borrow)
        return new_borrow
        
    
    
    def return_book(self, book_id, return_date:datetime):
        
        book = self.db.query(model.BorrowedBooks).filter(model.BorrowedBooks.book_id == book_id).first()
        
        
        book.return_date = return_date
        self.db.commit()
        self.db.refresh(book)
        
        return book
        
         
        