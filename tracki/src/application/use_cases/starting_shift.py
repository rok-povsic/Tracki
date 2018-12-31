import attr
import inject

from tracki.src.application import repositories
from tracki.src.domain import entities


class StartingShiftUseCase:
    @attr.s
    class InputDTO:
        category_id: str = attr.ib()

    _shifts_repo = inject.attr(repositories.ShiftRepository)

    def execute(self, input_dto: InputDTO) -> None:
        shift = entities.Shift(input_dto.category_id)
        shift.start()

        self._shifts_repo.save(shift)
