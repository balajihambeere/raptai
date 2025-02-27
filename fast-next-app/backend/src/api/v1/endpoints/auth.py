from datetime import timedelta
from typing import Annotated, Any
from fastapi import APIRouter, Depends, HTTPException, status
from core.security import create_access_token
from repositories.auth_repository import AuthRepository
from schemas.token import Token
from services.auth_service import AuthService
from fastapi.security import OAuth2PasswordRequestForm
from core.config import settings
from schemas.user import UserCreateRequest
from fastapi import Body

router = APIRouter(prefix="/auth", tags=["auth"])


def get_auth_service():
    auth_repository = AuthRepository()
    return AuthService(auth_repository)


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], auth_service: AuthService = Depends(get_auth_service)
) -> Token:
    print('user', form_data)
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
    user: UserCreateRequest, auth_service: AuthService = Depends(get_auth_service)
) -> Any:
    # Check if the username already exists
    # existing_user = await auth_service.get_user(form_data.username, form_data.password)
    # if existing_user:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="Username already registered",
    #     )

    newUser = await auth_service.register_user(user)

    if not newUser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"message": "User registered successfully"}
