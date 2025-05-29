import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# Load environment variables
load_dotenv()

# Create database engine with connection pool settings
engine = create_engine(
    os.getenv('DATABASE_URL'),
    pool_pre_ping=True,  # Enable connection health checks
    pool_recycle=3600,   # Recycle connections after 1 hour
    pool_size=5,         # Maintain 5 connections in the pool
    max_overflow=10      # Allow up to 10 additional connections
)

# Create session factory
session_factory = sessionmaker(bind=engine)
SessionLocal = scoped_session(session_factory)

# Create declarative base
Base = declarative_base()

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize models
def init_db():
    """Initialize database"""
    Base.metadata.create_all(bind=engine) 