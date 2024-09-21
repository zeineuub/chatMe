from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from backend.utils.token import get_current_user
from database.schemas import UserCreate, User, Friendship
from database.db import get_db
from database import models
import logging

router = APIRouter(tags=["users"])


def create_user(user_data: UserCreate, db: Session):
    new_user = models.User(**user_data.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=User, status_code=status.HTTP_200_OK)
def get_user(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user),):
    if id is not current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id={id} not found"
        )
    return user


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def user_update(
    id: int,
    user_data: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    user_update = db.query(models.User).filter(models.User.id == id).first()
    if not user_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id={id} not found"
        )
    user_update.update(**user_data.dict())
    db.commit()
    db.refresh(user_update)


@router.post(
    "/send-invitation/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=Friendship,
)
def send_invitation(
    id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    receiver = db.query(models.User).filter(models.User.id == id).first()
    if not receiver:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="the user you want to become friends with doesn't exist",
        )
    # create a friendship with pending status
    # check if the user already sent a friend request
    request_sent = (
        db.query(models.Friendship)
        .filter(
            models.Friendship.sender_id == current_user.id,
            models.Friendship.receiver_id == id,
        )
        .first()
    )
    if request_sent:
        logging.info("request already sent")
        return request_sent
    friendship = models.Friendship(sender_id=current_user.id, receiver_id=id)
    db.add(friendship)
    db.commit()
    return friendship


@router.put(
    "/confirm-invitation/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=Friendship,
)
def confirm_invitation(
    id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    sender = db.query(models.User).filter(models.User.id == id).first()
    if not sender:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="the user you receice a friend request doesn't exist",
        )

    request_received = (
        db.query(models.Friendship)
        .filter(
            models.Friendship.receiver_id == current_user.id,
            models.Friendship.sender_id == id,
        )
        .first()
    )
    if not request_received:
        logging.info("request dont exist")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="the user you receice a friend request doesn't exist",
        )
    request_received.status = models.Status.CONFIRMED
    db.add(request_received)
    db.commit()
    return request_received


@router.put(
    "/decline-invitation/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=Friendship,
)
def decline_invitation(
    id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    sender = db.query(models.User).filter(models.User.id == id).first()
    if not sender:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="the user you receice a friend request doesn't exist",
        )

    request_received = (
        db.query(models.Friendship)
        .filter(
            models.Friendship.receiver_id == current_user.id,
            models.Friendship.sender_id == id,
        )
        .first()
    )
    if not request_received:
        logging.info("request dont exist")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="the user you receice a friend request doesn't exist",
        )
    request_received.status = models.Status.DECLINED
    db.add(request_received)
    db.commit()
    return request_received
