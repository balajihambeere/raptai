from core.security import get_password_hash
from repositories.auth_repository import AuthRepository
from schemas.user import UserCreateRequest


class AuthService:
    def __init__(self, auth_repository: AuthRepository):
        self.auth_repository = auth_repository

    async def get_user(self,  username: str, password: str):
        return await self.auth_repository.authenticate_user(username, password)
    # return await self.auth_repository.get_user(username, password)

    async def register_user(self, user:UserCreateRequest):
        user_data = {"email": user.email, 
                     "fullname": user.fullname,
                     "password": get_password_hash(user.password)}
        return await self.auth_repository.register_user(user_data)
