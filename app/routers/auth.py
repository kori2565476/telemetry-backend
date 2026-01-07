from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session



from app.services.auth import authenticate_user
from app.core.security import create_access_token


from app.schemas.auth import LoginRequest, Token
from app.db import get_session

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Token)
def login(
    data: LoginRequest,
    session: Session = Depends(get_session),
):
    user = authenticate_user(session, data.email, data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    access_token = create_access_token(subject=str(user.id))

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
