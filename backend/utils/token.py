from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from database.db import get_db
from database.schemas import TokenData, UserCreate, User
from database import models
from .config import settings

# creating a jwt token
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login",
)


def create_access_token(data: dict) -> str:
    """
    Create an access token.
    """
    expiration_time = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    token_data = {**data, "exp": expiration_time}
    encoded_token = jwt.encode(
        token_data, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_token


def verify_access_token(token: str, credentials_exception) -> TokenData:
    """Verify the given access token."""
    try:
        print(token)
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        print(payload)
        user_id = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        return TokenData(user_id=user_id)
    except JWTError:
        raise credentials_exception


def get_current_user(
    access_token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> UserCreate | None:
    """
    Get user from access token
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_access_token(access_token, credentials_exception)
    user = db.query(models.User).get(token_data.user_id)
    if user is None:
        raise credentials_exception
    user = User.model_validate(user)
    return user
