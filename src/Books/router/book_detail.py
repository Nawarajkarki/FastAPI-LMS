from datetime import datetime
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse


from sqlalchemy.orm import Session
from src.entrypoint.database import get_db
from src.Books.service.service import BooksServices
from src.Books.service.borrow_service import BorrowService
from src.Books.schemas import schemas

detail = APIRouter(prefix='/api/books/{book_id}/details')











