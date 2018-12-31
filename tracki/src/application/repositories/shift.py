import abc

from tracki.src.domain import entities


class ShiftRepository:

    @abc.abstractmethod
    def save(self, shift: entities.Shift):
        pass
