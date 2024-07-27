from fastapi import APIRouter, Depends, HTTPException, status
from database.db import get_db
from database import models
from database.schemas import Post, User, PostCreate
from sqlalchemy.orm import Session
from typing import List
from backend.utils.token import get_current_user

router = APIRouter(tags=["posts"])


@router.post("/", response_model=Post, status_code=status.HTTP_201_CREATED)
def create_post(
    post_data: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a post"""
    post = models.Post(**post_data.dict(), user_id=current_user.id)
    db.add(post)
    db.commit()
    return post


@router.get("/{id}", response_model=Post, status_code=status.HTTP_200_OK)
def get_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get a single post"""
    post = (
        db.query(models.Post)
        .filter(models.Post.id == id, models.Post.user_id == current_user.id)
        .first()
    )
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} not found"
        )
    return post


@router.get("/", response_model=List[Post], status_code=status.HTTP_200_OK)
def get_all_posts(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    """Get all posts of a specific user"""
    posts = db.query(models.Post).filter(models.Post.user_id == current_user.id).all()
    return posts


@router.put("/{id}", response_model=Post, status_code=status.HTTP_200_OK)
def update_posts(
    id: int,
    post_data: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get all posts of a specific user"""
    post = (
        db.query(models.Post)
        .filter(models.Post.id == id, models.Post.user_id == current_user.id)
        .first()
    )
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} not found"
        )

    post.content = post_data.content
    db.commit()
    db.refresh(post)

    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get all posts of a specific user"""
    post = (
        db.query(models.Post)
        .filter(models.Post.id == id, models.Post.user_id == current_user.id)
        .first()
    )
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} not found"
        )

    db.delete(post)
    db.commit()
