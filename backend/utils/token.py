from fastapi import Depends, HTTPException,status
from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from database.db import get_db
from database.schemas import TokenData, User
from .config import settings
# creating a jwt token
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT")

def create_access_token(data: dict) -> str:
    """
    Create an access token.
    """
    expiration_time = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token_data = {**data, "exp": expiration_time}
    encoded_token = jwt.encode(token_data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_token

def verify_access_token(token: str, credentials_exception) -> TokenData:
    """Verify the given access token."""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        return TokenData(user_id=user_id)
    except JWTError as e:
        raise credentials_exception
 
def get_current_user(
        token: str = Depends(oauth2_scheme),
        db:Session=Depends(get_db), 
        credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials",headers={"WWW-Authenticate": "Bearer"}),
        
) -> User | None:
    """
    Get user from token
    """
    try:
        token = verify_access_token(token,credentials_exception)
        user = db.query(User).filter(User.id == token.user_id).first()
        return user
    except jwt.ExpiredSignatureError as e:
        raise Exception("Token expired", e)

