import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

engine = create_engine(
    os.getenv('DATABASE_URL'),
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_size=5,
    max_overflow=10
)

session_factory = sessionmaker(bind=engine)
SessionLocal = scoped_session(session_factory)

Base = declarative_base()

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initialize database"""
    Base.metadata.create_all(bind=engine) 