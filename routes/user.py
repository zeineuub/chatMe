from fastapi import APIRouter, HTTPException, logger,status
from database.schemas import UserCreate,User
from database.db import get_db
from database import models
router= APIRouter(
    prefix='/users',
    tags=['users'],
)

@router.post('/', response_class=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db=get_db()):
    new_use = models.User(**user.dict())
    db.add(new_use)
    db.commit()
    db.refresh(new_use)
    return new_use

@router.get('/{id}', response_class=User, status_code=status.HTTP_200_OK)
def get_user(id:int, db=get_db()):
    user = db.query(models.User).filter(id=id)
    if not user:
        logger('User not found')
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id={id} not found')
    return user

@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def user_update(id:int, user:UserCreate, db=get_db()):
    user_update = db.query(models.User).filter(id=id)
    if not user_update:
        logger('User not found')
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id={id} not found')
    user_update.update(user.dict())
    db.commit()