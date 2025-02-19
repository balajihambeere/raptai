from src.core.security import get_password_hash
from src.repositories.auth_repository import AuthRepository
from src.schemas.user import UserCreate


class AuthService:
    def __init__(self, auth_repository: AuthRepository):
        self.auth_repository = auth_repository

    async def get_user(self,  username: str, password: str):
        return await self.auth_repository.authenticate_user(username, password)
    # return await self.auth_repository.get_user(username, password)

    async def register_user(self, username: str, password: str):
        user_data = {"email": username,
                     "password": get_password_hash(password)}
        return await self.auth_repository.register_user(user_data)
