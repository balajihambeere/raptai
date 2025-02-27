from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.user_service import UserService
from repositories.user_repository import UserRepository
from schemas.user import UserCreateRequest, UserUpdate, User

router = APIRouter(prefix="/users", tags=["users"])


def get_user_service():
    user_repository = UserRepository()
    return UserService(user_repository)


@router.post("/", response_model=User)
async def create_user(user: UserCreateRequest, user_service: UserService = Depends(get_user_service)):
    return await user_service.create_user(user)


@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    db_user = await user_service.get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/", response_model=list[User])
async def read_users(skip: int = 0, limit: int = 100, user_service: UserService = Depends(get_user_service)):
    return await user_service.get_users(skip, limit)


@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserUpdate, user_service: UserService = Depends(get_user_service)):
    db_user = await user_service.update_user(user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/{user_id}", response_model=User)
async def delete_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    db_user = await user_service.delete_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
