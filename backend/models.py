from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    grade = Column(String)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index = True)
    username = Column(String, unique = True, index = True)
    hashed_password = Column(String)
    