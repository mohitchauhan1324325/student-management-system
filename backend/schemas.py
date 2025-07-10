from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int
    grade: str

class StudentOut(StudentCreate):
    id: int

    class Config:
        orm_mode = True
        
class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int 
    username: str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
