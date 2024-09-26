from enum import Enum
from typing import TypeVar, Generic, Type

from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorCollection
from pydantic import BaseModel

DbModel = TypeVar('DbModel', bound=BaseModel)


class BaseRepository(Generic[DbModel]):
    _entity_model: Type[DbModel]

    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection: AsyncIOMotorCollection = db.get_collection(self._entity_model._collection_name.default)

    @staticmethod
    def convert_enum_values(data):
        if isinstance(data, dict):
            return {k: BaseRepository.convert_enum_values(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [BaseRepository.convert_enum_values(item) for item in data]
        elif isinstance(data, Enum):
            return data.value
        else:
            return data

    async def create(self, data: dict, session=None) -> DbModel:
        validated_data = self._entity_model.model_validate(data)
        data_parsed_enums = self.convert_enum_values(validated_data.model_dump())
        data_parsed_enums["_id"] = data_parsed_enums.pop("id")
        await self.collection.insert_one(data_parsed_enums, session=session)
        return validated_data
