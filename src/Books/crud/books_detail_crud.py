from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.Books.models import model
from src.Books.schemas import book_detail_schemas

class BooksDetailCrud():
    
    def __init__(self, db:Session):
        self.db = db
        
    
    def get_detail(self, book_id:int):
        book_detail = self.db.query(model.BooksDetail).filter(model.BooksDetail.book_id == book_id).first()
        return book_detail
        
    
    
    def create_detail(self, book_detail : book_detail_schemas.BookDetailCreate):
        book_detail = model.BooksDetail(**book_detail.model_dump())
        self.db.add(book_detail)
        self.db.commit()
        self.db.refresh(book_detail)
        
        return book_detail
    
    
    def update_detail(self, book,  book_detail : book_detail_schemas.BooksDetailUpdate):
        
        if book_detail.num_of_pages is not None:
            book.num_of_pages = book_detail.num_of_pages
        if book_detail.language is not None:
            book.language = book_detail.language
            
        self.db.commit()
        self.db.refresh(book)
        return book
        