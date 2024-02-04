from pydantic import BaseModel, constr
from datetime import datetime
from typing import Optional

class BooksBase(BaseModel):
    title : constr(max_length=255)
    isbn : int
    published_date : datetime
    genre : Optional[constr(max_length=55)]
    
    

class BookCreate(BooksBase):
    pass
        
        
class Book(BooksBase):
    id : int
    
    class Config:
        from_attributes = True
        
        

class BookUpdate(BaseModel):
    title : constr(max_length=255) | None = None
    genre : constr(max_length=55) | None = None
    
    
    
    






class BorrowBookCreate(BaseModel):
    book_id: int
    user_id: int
    borrow_date: datetime
    
class BorrowedBooks(BorrowBookCreate):
    return_date: datetime | None = None
    
    
class ReturnBooks(BaseModel):
    user_id : int 
    book_id : int
    return_date : datetime