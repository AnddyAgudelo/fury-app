from fastapi import APIRouter, Request, Response

users_router: APIRouter = APIRouter(prefix="/users")


@users_router.post(
    path="",
    tags=["Users"],
    description="Endpoint to create users"
)
def create_user(request: Request, response: Response):
    pass


@users_router.get(
    path="",
    tags=["Users"],
    description="Get all users"
)
def get_all_users(request: Request, response: Response):
    pass
