from datetime import datetime
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse


from sqlalchemy.orm import Session
from src.entrypoint.database import get_db
from src.Books.service.borrow_service import BorrowService
from src.Books.schemas import schemas

borrow = APIRouter(prefix='/api/borrow', tags=['Borrowed Books'])


# Router for Borrowing and Returning books
@borrow.post('', response_model=schemas.BorrowedBooks)
def borrow_book(borrow_info:schemas.BorrowBookCreate, db:Session=Depends(get_db)):
    borrow_service = BorrowService(db)
    book_borrowed = borrow_service.borrow_book(borrow_info)
    return book_borrowed


@borrow.get('/borrowed/{user_id}', response_model=list[schemas.BorrowedBooks])
def books_borrowed_by_user(user_id:int, db:Session=Depends(get_db)):
    borrow_service = BorrowService(db)
    books = borrow_service.borrowed_by_user(user_id)
    return books



@borrow.put('/return', response_model=schemas.BorrowedBooks)
def return_book(return_info : schemas.ReturnBooks, db:Session = Depends(get_db)):
    borrow_service = BorrowService(db)
    return_book = borrow_service.return_book(return_info)
    return return_book


