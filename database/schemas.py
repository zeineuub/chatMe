from pydantic import BaseModel,EmailStr, Field

class Login(BaseModel):
    password:str
    email:str

class User(BaseModel):
    id:int
    fullname:str
    email:str
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name:str
    # Config class is used to convert dict to pydantic model
    class Config:
        # allows to use Pydantic models to interact with databases
        orm_mode = True
class TokenData(BaseModel):
    access_token: str
    user_id: int