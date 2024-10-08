from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.schemas import Login, UserCreate, User, Token
from database.db import get_db
from database import models
from backend.utils.hash import verify_password, get_password_hash
from backend.utils.token import create_access_token
from .users import create_user

router = APIRouter(tags=["authentication"])


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(login_data: Login, db: Session = Depends(get_db)):
    """Login user and return access token."""
    print(login_data)
    user = db.query(models.User).filter(models.User.email == login_data.email).first()
    if not user or not verify_password(login_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"user_id": str(user.id)})
    return {
        "access_token": access_token,
        "user": {
            "id": str(user.id),
            "email": user.email,
            "fullname": user.fullname 
        }
    }


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=User)
def register(user_data: UserCreate, db: Session = Depends(get_db)) -> User:
    """
    Register a new user and return the user object.
    """
    print(user_data)
    hashed_password = get_password_hash(user_data.password)
    user = create_user(
        UserCreate(
            firstname=user_data.firstname,
            lastname=user_data.lastname,
            email=user_data.email,
            password=hashed_password,
        ),
        db,
    )
    return user
