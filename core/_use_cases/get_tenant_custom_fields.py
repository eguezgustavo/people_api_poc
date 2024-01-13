import typing

from .. import _models
from .. import _repositories


class GetTenantCustomFields:
    def __init__(self, repository: _repositories.CustomFieldsRepository) -> None:
        self.repository: _repositories.CustomFieldsRepository = repository

    def __call__(self, tenant_id: str) -> typing.List[_models.CustomField]:
        return self.repository.get_all(tenant_id)
    