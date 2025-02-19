from sqlalchemy import Column, Integer, String
from database import Base

#defines how data will be stored in database

class Blog(Base):
    __tablename__ = "blogs"  # Add this line to specify the table name

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)


class User(Base):
    __tablename__= 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

