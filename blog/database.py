from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLAlchemy_Database_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLAlchemy_Database_URL, connect_args = {"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit= False, autoflush=False)

Base = declarative_base()


