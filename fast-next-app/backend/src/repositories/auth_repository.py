from src.core.security import verify_password
from src.models.user import User
from src.dependencies.database import database


class AuthRepository:
    async def get_user(self, email: str):
        query = User.select().where(User.c.email == email)
        # Use fetch_one instead of execute
        result = await database.fetch_one(query)
        if result:
            return dict(result)  # Convert to dictionary
        return None

    async def authenticate_user(self, username: str, password: str):
        user = await self.get_user(username)
        if not user:
            return False
        if not verify_password(password, user['password']):
            return False
        return user

    async def register_user(self, user: dict):
        query = User.insert().values(**user)
        user_id = await database.execute(query)
        return {"id": user_id, **user}
