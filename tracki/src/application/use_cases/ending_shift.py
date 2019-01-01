import inject

from tracki.src.application import repositories
from tracki.src.application.exceptions import shift as exceptions


class EndingShiftUseCase:

    _shifts_repo = inject.attr(repositories.ShiftRepository)

    def execute(self) -> None:
        shift = self._shifts_repo.get_last()
        if not shift.is_running:
            raise exceptions.ShiftNotRunningException
        shift.end()
        self._shifts_repo.save(shift)
