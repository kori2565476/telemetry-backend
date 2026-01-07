from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlmodel import Session

from app.core.config import settings
from app.database import get_session
from app.models.user import User
from app.schemas.auth import TokenPayload
from app.core.security import oauth2_scheme

def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
        token_data = TokenPayload(**payload)
    except JWTError:
        raise credentials_exception

    if token_data.sub is None:
        raise credentials_exception

    user = session.get(User, int(token_data.sub))
    if not user:
        raise credentials_exception

    return user

