import typing

from .. import _models
from .. import _repositories


class CreateCustomField:
    def __init__(self, repository: _repositories.CustomFieldsRepository) -> None:
        self.repository: _repositories.CustomFieldsRepository = repository

    def __call__(
        self,
        name: str,
        tenant_id: str,
        required: bool,
        visibility: typing.List[str],
        field_type: str,
        config: typing.Any,
    ) -> _models.ShortTextField:
        field_roles = [_models.Role(name=role_name) for role_name in visibility]
        to_create = _models.CustomField(
            field_id=None,
            name=name,
            tenant_id=tenant_id,
            required=required,
            visibility=field_roles,
            field_type=field_type,
            config=config
        )
        return self.repository.create(to_create)
    