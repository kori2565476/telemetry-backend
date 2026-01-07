
from sqlmodel import Session

from app.core.security import verify_password
from app.crud.user import get_user_by_email


def authenticate_user(
    session: Session,
    email: str,
    password: str
):
    user = get_user_by_email(session, email)
    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user

