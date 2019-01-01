import datetime
from unittest import mock

import freezegun

from tracki.src.application import use_cases
from tracki.src.domain import entities


def test_should_end_shift(shift_repo_mock: mock.Mock) -> None:
    shift_repo_mock.get_last.return_value = entities.Shift(
        category=entities.Category(name='A'),
        start_time=datetime.datetime(2010, 1, 1),
    )

    with freezegun.freeze_time('2010-01-01 00:05'):
        use_cases.EndingShiftUseCase().execute()

    shift_repo_mock.save.assert_called_once_with(
        entities.Shift(
            category=entities.Category('A'),
            start_time=datetime.datetime(2010, 1, 1),
            end_time=datetime.datetime(2010, 1, 1, 0, 5),
        )
    )
