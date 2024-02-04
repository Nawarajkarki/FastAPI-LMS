from datetime import datetime
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse


from sqlalchemy.orm import Session
from src.entrypoint.database import get_db
from src.Books.service.service import BooksServices
from src.Books.service.book_detail_service import BooksDetailServices
from src.Books.schemas import schemas
from src.Books.schemas import book_detail_schemas

book = APIRouter(prefix='/api/books', tags=['Books'])



@book.get('/', response_model=list[schemas.Book])
def get_all_books(db:Session = Depends(get_db)):
    book_service = BooksServices(db)
    books = book_service.get_book(book_id=None)
    
    return books

@book.get('/{book_id}', response_model=schemas.Book )
def get_book(book_id : int, db: Session = Depends(get_db)):
    book_service = BooksServices(db)
    
    book = book_service.get_book(book_id)
    
    return book
    
@book.post('/', response_model=schemas.Book)
def create_book(book:schemas.BookCreate, db:Session = Depends(get_db)):
    
    book_service = BooksServices(db)
    new_book = book_service.create_new_book(book)
    return new_book

@book.put('/{book_id}', response_model=schemas.Book)
def update_book(book_id, book_info:schemas.BookUpdate, db:Session =Depends(get_db)):
    book_service = BooksServices(db)
    updated_book = book_service.update_book_info(book_id=book_id, book= book_info)
    
    return updated_book
    
@book.delete('/{book_id}')
def delete_book(book_id:int, db:Session=Depends(get_db)):
    book_service = BooksServices(db)
    
    book_service.delete_book(book_id)
    return JSONResponse(
            status_code=status.HTTP_200_OK, 
            content="Book deleted"
        )





@book.put('/{book_id}/details', response_model=book_detail_schemas.BookDetail)
def update_book_detail(book_id:int, new_detail:book_detail_schemas.BooksDetailUpdate ,db:Session=Depends(get_db)):
    detail_service = BooksDetailServices(db)
    book_details = detail_service.update_detail(book_id, new_detail)
    
    return book_details

@book.get('/{book_id}/details', response_model=book_detail_schemas.BookDetail)
def get_book_detail(book_id:int, db:Session=Depends(get_db)):
    detail_service = BooksDetailServices(db)
    book_detail = detail_service.get_book_detail(book_id)
    
    return book_detail


@book.post('/{book_id}/details', response_model=book_detail_schemas.BookDetail)
def add_book_detail(book_id:int,  details : book_detail_schemas.BookDetailCreate ,db:Session=Depends(get_db)):
    detail_service = BooksDetailServices(db)
    new_detail = detail_service.create_detail(book_id, details)
    
    return new_detail

