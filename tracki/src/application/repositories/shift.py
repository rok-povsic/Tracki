import abc

from tracki.src.domain import entities


class ShiftRepository:

    @abc.abstractmethod
    def save(self, shift: entities.Shift) -> None:
        pass

    @abc.abstractmethod
    def get_last(self) -> entities.Shift:
        pass
