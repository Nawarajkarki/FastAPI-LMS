from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from src.Books.crud.borrow_crud import BorrowBooks
from src.Books.schemas import schemas
from src.Users.service.service import UserServices
from src.Books.service.service import BooksServices

class BorrowService():
    
    def __init__(self, db:Session):
        self.borrow_crud = BorrowBooks(db)
        self.user_service = UserServices(db)
        self.book_service = BooksServices(db)
        
    
    def borrowed_by_user(self, user_id:int):
        
        user = self.user_service.get_user_by_id(user_id)
        
        borrowed_books = self.borrow_crud.get_borrowed_books_by_user(user_id)
        
        if not borrowed_books:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content="User hasn't borrowed any books"
            )
            
        return borrowed_books
    

    
    def borrow_book(self, borrow_info:schemas.BorrowBookCreate):
        
        
        user = self.user_service.get_user_by_id(borrow_info.user_id)
        book = self.book_service.get_book(borrow_info.book_id)
        
        
        is_borrowed = self.borrow_crud.is_borrowed(borrow_info.book_id)
        print(is_borrowed)
        
        if is_borrowed:
            raise HTTPException(status_code=404, detail="Book not available for borrow.")
        
        borrowed_book = self.borrow_crud.borrow_book(borrow_info)
        return borrowed_book
    
    
    
    def return_book(self, return_info : schemas.ReturnBooks):
        user_id = return_info.user_id
        book_id = return_info.book_id
        return_date = return_info.return_date
        
        user = self.user_service.get_user_by_id(user_id=user_id)
        book = self.book_service.get_book(book_id=book_id)
        
        
        
        # book = self.book_service.get_book(book_id)
        
        is_borrowed = self.borrow_crud.is_borrowed(book_id=book_id)
        if not is_borrowed:
            raise HTTPException(status_code=400, detail="Book isn't borrowed yet.")
        
        returned_book = self.borrow_crud.return_book(book_id, return_date)
        return returned_book
        
        