import uvicorn
from fastapi import FastAPI

from api.users.controllers.users_controller import users_router
from core.config import settings

app = FastAPI()

app.include_router(users_router, prefix=settings.API_STR)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
