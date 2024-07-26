from fastapi import APIRouter, HTTPException, logger,status,Depends
from database.schemas import UserCreate,User
from database.db import get_db
from database import models
router= APIRouter(
    prefix='/users',
    tags=['users'],
)

def create_user(user_data: UserCreate, db=Depends(get_db())):
    new_user = models.User(**user_data.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', response_class=User, status_code=status.HTTP_200_OK)
def get_user(id:int,  db=Depends(get_db())):
    user = db.query(models.User).filter(id=id)
    if not user:
        logger('User not found')
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id={id} not found')
    return user

@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def user_update(id:int, user_data:UserCreate,  db=Depends(get_db())):
    user_update = db.query(models.User).filter(id=id)
    if not user_update:
        logger('User not found')
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id={id} not found')
    user_update.update(user_data.dict())
    db.commit()