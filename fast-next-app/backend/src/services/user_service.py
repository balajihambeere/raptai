from repositories.user_repository import UserRepository
from schemas.user import UserCreateRequest, UserUpdate


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def get_user(self, user_id: int):
        return await self.user_repository.get_user(user_id)

    async def get_users(self, skip: int = 0, limit: int = 100):
        return await self.user_repository.get_users(skip, limit)

    async def create_user(self, user: UserCreateRequest):
        user_data = user.model_dump()
        return await self.user_repository.create_user(user_data)

    async def update_user(self, user_id: int, user: UserUpdate):
        user_data = user.model_dump(exclude_unset=True)
        return await self.user_repository.update_user(user_id, user_data)

    async def delete_user(self, user_id: int):
        return await self.user_repository.delete_user(user_id)
