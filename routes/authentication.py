from fastapi import APIRouter, HTTPException, logger,status
from database.schemas import Login,UserCreate,User,Token
from database.db import get_db
from database import models
from backend.chore.hash import verify_password, get_password_hash
from backend.chore.token import create_access_token
router = APIRouter(
    '/auth',
    tags=['authentication']
)
@router.post('/login', status_code=status.HTTP_200_OK)
def login(user:Login,db=get_db()):
    found_user = db.query(models.User).filter(email=user.email).first()
    if not found_user:
        logger('User not found')
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id={id} not found')
    if not verify_password(user.password, found_user.password):
        logger('The passwerd in not correct')
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The passwerd in not correct')
    access_token = create_access_token(
        data={"sub": user.id}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
    # generate a token

@router.post('/register',status_code=status.HTTP_200_OK,response_model=User)
def register(user:UserCreate,db=get_db()):
    hashed_password = get_password_hash(user.password)
    new_user = {
        'firstname':user.firstname,
        'lastname':user.lastname,
        'email':user.email,
        'password':hashed_password
    }
    user= models.User(**new_user)
    return user
