import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from database.schemas import TokenData
from .config import settings
# creating a jwt token
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    # data is the payload u want to encode
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verufy_access_token(token: str, credentials_exception):
    payload = jwt.decode(token,settings.SECRET_KEY,settings.ALGORITHM)
    user_id = payload.get(id)
    if user_id is None:
        raise credentials_exception
    token_data = TokenData(id=id)
    return token_data
     
