# SQLAlchemy utilities
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

# Create a new SQLite database connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Factory for creating new database sessions (transactions)
SessionLocal = sessionmaker(bind=engine)

# Base class for our models (tables)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
