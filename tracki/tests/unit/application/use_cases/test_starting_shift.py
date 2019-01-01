import datetime
from unittest import mock

import freezegun

from tracki.src.application import use_cases
from tracki.src.domain import entities


def test_should_save_shift_start(shift_repo_mock: mock.Mock) -> None:
    input_dto = use_cases.StartingShiftUseCase.InputDTO(
        category=entities.Category(name='category1')
    )

    with freezegun.freeze_time('2010-01-01'):
        use_cases.StartingShiftUseCase().execute(input_dto)

    shift_repo_mock.save.assert_called_once_with(
        entities.Shift(
            category=entities.Category('category1'), start_time=datetime.datetime(2010, 1, 1)
        )
    )
