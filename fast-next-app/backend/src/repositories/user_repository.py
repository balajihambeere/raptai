from models.user import User
from dependencies.database import database


class UserRepository:

    async def get_user(self, user_id: int):
        query = User.select().where(User.c.id == user_id)
        # Use fetch_one instead of execute
        result = await database.fetch_one(query)
        if result:
            return dict(result)  # Convert to dictionary
        return None

    async def get_users(self, skip: int = 0, limit: int = 100):
        query = User.select().offset(skip).limit(limit)
        # Use fetch_all instead of execute
        results = await database.fetch_all(query)
        return [dict(row) for row in results]  # Convert each row to dictionary

    async def create_user(self, user: dict):
        query = User.insert().values(**user)
        user_id = await database.execute(query)
        return {"id": user_id, **user}

    async def update_user(self, user_id: int, user: dict):
        query = User.update().where(User.c.id == user_id).values(**user)
        await database.execute(query)
        # Return updated user data
        return {"id": user_id, **user}

    async def delete_user(self, user_id: int):
        query = User.delete().where(User.c.id == user_id)
        await database.execute(query)
        return {"id": user_id, "deleted": True}
