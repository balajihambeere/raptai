from datetime import timedelta
from typing import Annotated, Any
from fastapi import APIRouter, Depends, HTTPException, status
from src.core.security import create_access_token
from src.repositories.auth_repository import AuthRepository
from src.schemas.token import Token
from src.services.auth_service import AuthService
from fastapi.security import OAuth2PasswordRequestForm
from src.core.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])


def get_auth_service():
    auth_repository = AuthRepository()
    return AuthService(auth_repository)


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], auth_service: AuthService = Depends(get_auth_service)
) -> Token:
    user = await auth_service.get_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user['email']}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post("/register")
async def register_new_user(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], auth_service: AuthService = Depends(get_auth_service)
) -> Any:
    # Check if the username already exists
    # existing_user = await auth_service.get_user(form_data.username, form_data.password)
    # if existing_user:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="Username already registered",
    #     )

    user = await auth_service.register_user(form_data.username, form_data.password)
    print('user', user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"message": "User registered successfully"}
