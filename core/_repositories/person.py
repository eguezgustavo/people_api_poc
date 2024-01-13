import abc
import typing

from .. import _models


class PersonRepository(abc.ABC):

    @abc.abstractmethod
    def create(self, person: _models.Person) -> _models.Person:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, person_di: str) -> _models.Person:
        raise NotImplementedError
