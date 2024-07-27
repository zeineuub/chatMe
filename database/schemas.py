from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class Base(BaseModel):
    created_at: datetime = datetime.now()
class Login(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True

class User(Base):
    id: int
    fullname: str
    email: EmailStr

    class Config:
        from_attributes = True

class UserCreate(Base):
    email: EmailStr
    password: str
    firstname: str
    lastname: str

    class Config:
        from_attributes = True

class Token(Base):
    access_token: str
    token_type: str

class TokenData(Base):
    user_id: Optional[str] = None

class PostCreate(Base):
    id:int
    content:str
    created_by: User