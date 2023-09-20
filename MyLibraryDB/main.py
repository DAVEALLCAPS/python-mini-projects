# Importing required FastAPI utilities and dependencies
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session  # To use SQLAlchemy session for database interactions
import crud, models, database  # Importing the CRUD operations, models, and database utilities
from database import get_db

# Creating an instance of the FastAPI application
app = FastAPI()

# Creating the tables in the SQLite database based on the defined models
models.Base.metadata.create_all(bind=database.engine)

# Route to add a new book to the database
@app.post("/books/")
def create_book(book: models.BookSchema, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book_data=book.dict())

# Route to fetch a list of books from the database with optional skip and limit parameters
@app.get("/books/")
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):  # Default values for pagination
    books = crud.get_books(db, skip=skip, limit=limit)  # Use the CRUD function to fetch books
    return books
