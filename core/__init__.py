import typing

from ._repositories import CustomFieldsRepository, PersonRepository
from ._models import CustomField, ShortTextField, Person
from . import _use_cases

class PeopleAPICore:
    def __init__(
        self,
        custom_fields_repository: CustomFieldsRepository,
        person_repository: PersonRepository
    ) -> None:
        self.custom_fields_repository = custom_fields_repository
        self.person_repository = person_repository

    def  create_custom_field(
        self,
        name: str,
        tenant_id: str,
        required: bool,
        visibility: typing.List[str],
        field_type: str,
        config: typing.Any,
    ) -> _models.ShortTextField:
        create_field = _use_cases.CreateCustomField(self.custom_fields_repository)
        return create_field(
            name=name,
            tenant_id=tenant_id,
            required=required,
            visibility=visibility,
            field_type=field_type,
            config=config,
        )

    def get_all_for_tenant(self, tenant_id: str) -> typing.List[CustomField]:
        get_all = _use_cases.GetTenantCustomFields(self.custom_fields_repository)
        return get_all(tenant_id)

    def create_person(self, tenant_id: str, name: str, last_name: str, **custom_fields) -> _models.Person:
        create_person = _use_cases.CreatePerson(self.person_repository, self.custom_fields_repository)
        return create_person(tenant_id=tenant_id, name=name, last_name=last_name, **custom_fields)

    def get_person(self, person_id: str) -> _models.Person:
        get_person = _use_cases.GetPerson(self.person_repository)
        return get_person(person_id)
