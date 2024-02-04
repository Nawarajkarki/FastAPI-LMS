from fastapi import FastAPI

from src.Users.router.router import user
from src.Books.router.router import book
from src.Books.router.borrow_router import borrow



app = FastAPI()

# Router of other Apps
app.include_router(user)
app.include_router(book)
app.include_router(borrow)

@app.get('/')
def home():
    return "Diabolical... . . .  .   .   .   .    .     .      .       .       .         .             .             .              ."