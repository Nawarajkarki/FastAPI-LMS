from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from src.Books.crud.books_detail_crud import BooksDetailCrud
from src.Books.schemas import book_detail_schemas
from src.Users.service.service import UserServices
from src.Books.service.service import BooksServices



class BooksDetailServices():
    
    def __init__(self, db:Session):
        self.crud = BooksDetailCrud(db)
        self.book_service = BooksServices(db)
        
        
    def get_book_detail(self, book_id:int):
        book = self.book_service.get_book(book_id)
        
        
        detail = self.crud.get_detail(book_id)
        print(f"detail = {detail}")
        if detail is None:
            raise HTTPException(status_code=404, detail="No book Details")
        return detail
        
        
 
    def create_detail(self, book_id:int, details:book_detail_schemas.BookDetailCreate):
        
        # book = self.book_service.get_book(book_id)
        book = self.book_service.get_book(book_id)
        book_detail = self.get_book_detail(book_id)
        if book_detail is not None:
            raise HTTPException(status_code=400, detail="Detial already exists")
        
        
        book_details = self.crud.create_detail(details)
        return book_details
    
    
    
    def update_detail(self,book_id:int, detail:book_detail_schemas.BooksDetailUpdate):
        book = self.book_service.get_book(book_id)
        book_obj = self.get_book_detail(book_id)
        
        new_detail = self.crud.update_detail(book_obj, detail)
        
        return new_detail