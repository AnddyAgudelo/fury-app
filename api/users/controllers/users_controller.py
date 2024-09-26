from fastapi import APIRouter, Request, Response

from api.users.schemas.inputs import UserInput
from api.users.services.users_service import UsersService

users_router: APIRouter = APIRouter(prefix="/users")


@users_router.post(
    path="",
    tags=["Users"],
    description="Endpoint to create users"
)
async def create_user(
        request: Request,
        response: Response,
        user_input: UserInput,
):
    print("Creating user in controller")
    user_service = UsersService(request.app.database)
    user = await user_service.create_user(user_input)
    print("Created user")
    return user


@users_router.get(
    path="",
    tags=["Users"],
    description="Get all users"
)
def get_all_users(request: Request, response: Response):
    pass
