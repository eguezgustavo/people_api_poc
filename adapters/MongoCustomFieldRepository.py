import json
import typing

from pymongo import MongoClient

import core

_CONNECTION_STRING = "mongodb://root:example@mongodb:27017"


class MongoCustomFieldRepository(core.CustomFieldsRepository):
    def __init__(self) -> None:
        mongo_client = MongoClient(_CONNECTION_STRING)
        db = mongo_client["test"]
        self.custom_fields = db["custom_fields"]

    def create(self, field: core.CustomField) -> core.CustomField:
        to_create = field._asdict()
        to_create.pop("field_id")
        to_create["config"] = json.dumps(field.config)

        self.custom_fields.insert_one(to_create)
        created_field = self.__transform_mongo_response(to_create)

        return core.CustomField(**created_field)

    def get_all(self, tenant_id: str) -> typing.List[core.CustomField]:
        all_custom_fiels = self.custom_fields.find({"tenant_id": tenant_id})
        return [
            core.CustomField(**self.__transform_mongo_response(custom_field))
            for custom_field in all_custom_fiels
        ]

    def __transform_mongo_response(self, mongo_response):
        mongo_response["field_id"] = str(mongo_response["_id"])
        mongo_response.pop("_id")

        return mongo_response