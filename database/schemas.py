from pydantic import BaseModel,EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name:str
    # Config class is used to convert dict to pydantic model
    class Config:
        # allows to use Pydantic models to interact with databases
        orm_mode = True
class Auth(BaseModel):
    password:str
    email:EmailStr
    class Config:
        orm_mode = True
class Authorize(BaseModel):
    token:str
class PostCreate(BaseModel):
    content:str
    class Config:
        orm_mode = True
