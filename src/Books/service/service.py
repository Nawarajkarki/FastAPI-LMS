from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from src.Books.crud.book import BooksCrud
from src.Books.schemas import schemas


# book Services
class BooksServices():
    
    def __init__(self, db:Session):
        self.crud = BooksCrud(db)
        
        
    
    def get_book(self, book_id:int | None = None):
        
        book = self.crud.get_books(book_id=book_id)
        
        if book is None :
            raise HTTPException(status_code=404, detail=f"book with book ID -- {book_id} doesnot exist.")
        elif not book:
            raise HTTPException(status_code=404, detail="book table is empty")
        
        return book
    
    
    def create_new_book(self, book : schemas.BookCreate):
        
        obj = self.crud.get_book_by_isbn(book.isbn)

        if obj is not None:
            raise HTTPException(status_code=400, detail="book with isbn already exists")
        
        new_book = self.crud.create_book(book=book)
        return new_book
    
    
    
    def update_book_info(self, book_id:int,  book : schemas.BookUpdate):
        
        obj = self.crud.get_books(book_id)
        if obj is None:
            raise HTTPException(status_code=400, detail="book doesn't exist" )
        
        updated_book = self.crud.update_book_info(book_obj=obj, title=book.title, genre=book.genre)
        return updated_book 
    
    
    def delete_book(self, book_id:int):
        
        book = self.crud.get_books(book_id=book_id)
        
        if book is None :
            raise HTTPException(status_code=404, detail=f"book with book ID -- {book_id} doesnot exist.")
        
        removal = self.crud.delete_book(book)
        return JSONResponse(
            status_code=status.HTTP_204_NO_CONTENT, 
            content="book deleted"
        )