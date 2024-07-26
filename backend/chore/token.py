import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from database.schemas import TokenData, User
from .config import settings
# creating a jwt token
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)) -> str:
    """
    Create an access token.

    Args:
        data (dict): Additional data to include in the token.
        expires_delta (timedelta, optional): Time until the token expires. Defaults to 15 minutes.

    Returns:
        str: The encoded access token.
    """
    expiration_time = datetime.now(timezone.utc) + expires_delta
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
    except jwt.ExpiredSignatureError as e:
        raise Exception("Token expired", e)
 
def get_user_from_token(token: str, credentials_exception, db) -> User | None:
    """
    Get user from token

    Args:
        token (str): Token string
        credentials_exception: Exception to raise if token is invalid
        db (Session): Database session

    Returns:
        User: User object if token is valid, None otherwise
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        user = db.query(User).filter(User.id == user_id).first()
        return user
    except jwt.ExpiredSignatureError as e:
        raise Exception("Token expired", e)

