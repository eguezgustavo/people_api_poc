import typing

from .. import _models
from .. import _repositories


class CreatePerson:
    def __init__(
        self,
        repository: _repositories.PersonRepository,
        custom_fields_repository: _repositories.CustomFieldsRepository,
    ) -> None:
        self.repository = repository
        self.custom_fields_repository = custom_fields_repository

    def __call__(self, tenant_id: str, name: str, last_name: str, **custom_fields) -> _models.Person:
        return self.repository.create(
            _models.Person(
                person_id=None,
                name=name,
                last_name=last_name,
                tenant_id=tenant_id,
                custom_fields=self.__build_custom_fields(tenant_id, **custom_fields),
            )
        )

    def __build_custom_fields(self, tenant_id: str, **custom_fields_data) -> typing.Dict[str, typing.Any]:
        fields_factories_for_tenant = self.custom_fields_repository.get_factories_for(tenant_id=tenant_id)

        custom_fields = {}
        for field_name, field_value in custom_fields_data.items():
            field_factory = fields_factories_for_tenant[field_name]["factory"]
            field_id = fields_factories_for_tenant[field_name]["field_id"]
            custom_fields[field_name] = field_factory(field_id=field_id, value=field_value)
        
        return custom_fields
