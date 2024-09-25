import uvicorn
from fastapi import FastAPI

from api.users.controllers.users_controller import users_router

app = FastAPI()

app.include_router(users_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
