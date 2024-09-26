from pydantic import EmailStr

from models.base_model import DBBaseModel


class UsersModel(DBBaseModel):
    _collection_name = "users"

    first_name: str
    last_name: str
    email: EmailStr
    password: str
