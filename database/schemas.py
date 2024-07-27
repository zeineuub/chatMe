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


class UserBase(Base):
    id: int
    email: str
    firstname: str
    lastname: str

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    pass


class Token(Base):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[str] = None


class Post(Base):
    id: int
    content: str
    user_id: int


class PostCreate(BaseModel):
    content: str
