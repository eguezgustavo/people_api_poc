import typing

from .custom_field import CustomField


class Person(typing.NamedTuple):
    person_id: str | None
    name: str
    last_name: str
    tenant_id: str
    custom_fields: typing.Dict[str, typing.Any]
