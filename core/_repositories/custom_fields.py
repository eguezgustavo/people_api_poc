import abc
import typing

from .. import _models


class CustomFieldsRepository(abc.ABC):

    @abc.abstractmethod
    def create(self, field: _models.CustomField) -> _models.CustomField:
        raise NotImplementedError

    @abc.abstractmethod
    def get_all(self, tenant_id: str) -> typing.List[_models.CustomField]:
        raise NotImplementedError

    def get_factories_for(self, tenant_id: str) -> typing.Dict[str, typing.Dict]:
        tenant_custom_fields = self.get_all(tenant_id=tenant_id)
        return {
            custom_field.name: {
                "field_id": custom_field.field_id,
                "factory": self.__get_factory(custom_field.field_type),
            }
            for custom_field in tenant_custom_fields
        }

    def __get_factory(self, field_type: str) -> typing.Callable:
        factories = {
            "short_text": _models.ShortTextField,
            "multi_select":_models.MultiSelectField,
        }

        return factories.get(field_type)
