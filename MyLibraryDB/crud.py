# SQLAlchemy session for DB operations
from sqlalchemy.orm import Session
import models

# Function to create a new book entry
def create_book(db: Session, book_data: dict):
    db_book = models.Book(**book_data)  # Convert dict to models.Book instance
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Function to retrieve a list of books
def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()  # Query to get books with offset and limit
