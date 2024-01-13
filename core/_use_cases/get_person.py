import typing

from .. import _models
from .. import _repositories


class GetPerson:
    def __init__(
        self,
        repository: _repositories.PersonRepository,
    ) -> None:
        self.repository = repository
        self.custom_fields_repository = None

    def __call__(self, person_id: str) -> _models.Person:
        return self.repository.get(person_id)
