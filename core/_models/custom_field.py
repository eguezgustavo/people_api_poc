import typing

from .role import Role
    

class CustomField(typing.NamedTuple):
    field_id: str | None
    name: str
    tenant_id: str
    required: bool
    visibility: typing.List[Role]
    field_type: str
    config: typing.Any


class ShortTextField(typing.NamedTuple):
    field_id: str
    value: str


class MultiSelectField(typing.NamedTuple):
    field_id: str
    value: typing.List
