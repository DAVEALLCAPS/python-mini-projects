# Import necessary libraries and utilities from SQLAlchemy
from sqlalchemy import Column, Integer, String
from database import Base  # Importing the base class for ORM models
from pydantic import BaseModel  # Importing the base class for Pydantic models

# SQLAlchemy ORM model for the Book table in the database
class Book(Base):
    __tablename__ = "books"  # Name of the table in the database

    # Defining the columns for the table
    id = Column(Integer, primary_key=True, index=True)  # Primary key for the book
    title = Column(String, index=True)  # Title column, indexed for faster queries
    author = Column(String)  # Author column
    year_published = Column(Integer)  # Year the book was published column

# Pydantic model for validating and serializing Book data
class BookSchema(BaseModel):
    id: int  # Primary key for the book
    title: str  # Title of the book
    author: str  # Author of the book
    year_published: int  # Year the book was published

    class Config:
        from_attributes = True  # Allows automatic conversion from SQLAlchemy model to Pydantic model
