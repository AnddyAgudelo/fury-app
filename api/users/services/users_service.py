from motor.motor_asyncio import AsyncIOMotorDatabase

from api.users.schemas.inputs import UserInput
from repositories.users import UsersRepository


class UsersService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.users_repository = UsersRepository(self.db)

    async def create_user(self, user_input: UserInput):
        print("Creating user")
        user = await self.users_repository.create(user_input.model_dump())
        print(f"user: {user}")
        return user
