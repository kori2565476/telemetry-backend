from sqlmodel import Session, select
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

def get_user_by_email(db: Session, email: str)->User | None:
    statement = select(User).where(User.email == email)
    return db.exec(statement).first()

def create_user(db: Session, user_in: UserCreate)->User:

    existing_user = get_user_by_email(db, user_in.email)
    if existing_user:
        raise ValueError("Email already registered")
    
    user = User(
        email=user_in.email,
        hashed_password=hash_password(user_in.password),
        is_active=True,
    )
                                                                                                                                                                
    db.add(user)
    db.commit()
    db.refresh(user)
    return user