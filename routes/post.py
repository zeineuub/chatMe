from fastapi import APIRouter,Depends, HTTPException,status
from database.db import get_db
from database.models import Post
from database.schemas import UserCreate
from sqlalchemy.orm import Session
from database.schemas import PostCreate
from typing import List
from backend.utils.token import get_current_user,verify_access_token
router = APIRouter(
    tags=['posts']
)
@router.post('/', response_model=PostCreate, status_code=status.HTTP_201_CREATED)
def create_post(post_data:PostCreate,db:Session=Depends(get_db),current_user:UserCreate=Depends(get_current_user)):
    """ Create a post """
    post = Post(**post_data.dict())
    db.add(post)
    db.commit()
    return post
@router.post('/{id}', response_model=PostCreate, status_code=status.HTTP_201_CREATED)
def get_post(id:int,db:Session=Depends(get_db),current_user:UserCreate =Depends(get_current_user)):
    """ Get a single post"""
    post = db.query(Post).filter({'id':id,'user_id':current_user.id}).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id={id} not found')
    return post

@router.post('/', response_model=List[PostCreate], status_code=status.HTTP_201_CREATED)
def get_all_posts(db:Session=Depends(get_db),current_user:UserCreate =Depends(get_current_user)):
    """ Get all posts of a specific user"""
    posts = db.query(Post).filter(user_id =current_user.id).all()
    return posts

