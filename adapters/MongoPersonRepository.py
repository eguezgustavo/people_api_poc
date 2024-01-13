import typing

from pymongo import MongoClient
from bson.objectid import ObjectId

import core

_CONNECTION_STRING = "mongodb://root:example@mongodb:27017"


class MongoPersonRepository(core.PersonRepository):
    def __init__(self) -> None:
        mongo_client = MongoClient(_CONNECTION_STRING)
        db = mongo_client["test"]
        self.people = db["people"]

    def create(self, person: core.Person) -> core.Person:
        to_create = self.__map_person_to_dict(person)
        to_create.pop("person_id")

        self.people.insert_one(to_create)
        created_person = self.__transform_mongo_response(to_create)

        return self.__map_dict_to_person(created_person)

    def get(self, person_id: str) -> core.Person:
        person = self.people.find_one({"_id": ObjectId(person_id)})
        person = self.__transform_mongo_response(person)
        return self.__map_dict_to_person(person)

    def __map_person_to_dict(self, person: core.Person) -> typing.Dict:
        person_default_fields = {
            field: value for field, value in person._asdict().items() if field != "custom_fields"
        }
        custom_fields = {
            custom_field_name: {
                "field_id": custom_field.field_id,
                "value": custom_field.value,
            }
            for custom_field_name, custom_field in person.custom_fields.items()
        }

        return {
            **person_default_fields,
            **custom_fields,
        }

    def __map_dict_to_person(self, person: typing.Dict) -> core.Person:
        default_fields = ["person_id", "name", "last_name", "tenant_id"]
        person_default_fields = {
            field: value for field, value in person.items() if field in default_fields
        }
        custom_fields = {
            field: field_data["value"] for field, field_data in person.items() if field not in default_fields
        }

        return core.Person(**person_default_fields, custom_fields=custom_fields)

    def __transform_mongo_response(self, mongo_response):
        mongo_response["person_id"] = str(mongo_response["_id"])
        mongo_response.pop("_id")

        return mongo_response
