from fastapi import APIRouter, Depends, HTTPException, logger,status
from database.schemas import Login,UserCreate,User,Token
from database.db import get_db
from database import models
from backend.chore.hash import verify_password, get_password_hash
from backend.chore.token import create_access_token
from backend.chore.config import settings
from users import create_user
router = APIRouter(
    '/auth',
    tags=['authentication']
)
@router.post("/login", status_code=status.HTTP_200_OK, response_model=Token)
async def login(login_data: Login, db = Depends(get_db)):
    """Login user and return access token."""

    user = db.query(models.User).filter(models.User.email == login_data.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    if not verify_password(login_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect password"
        )

    access_token = create_access_token(
        data={"sub": user.id}, expires_delta=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    return Token(access_token=access_token, user_id=user.id)

@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=User)
def register(user_data: UserCreate, db=Depends(get_db)) -> User:
    """
    Register a new user and return the user object.
    """
    hashed_password = get_password_hash(user_data.password)
    user = create_user(
        UserCreate(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            password=hashed_password,
        ),
        db,
    )
    return user

