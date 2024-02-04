from pydantic import BaseModel, constr


class BookDetailBase(BaseModel):
    book_id : int
    num_of_pages : int
    publisher : constr(max_length=50)
    language : constr(max_length=10)

    

class BookDetailCreate(BookDetailBase):
    pass


class BookDetail(BookDetailBase):
    id : int
    

class BooksDetailUpdate(BaseModel):
    num_of_pages : int | None = None
    language : constr(max_length=10) | None = None   
     

    
