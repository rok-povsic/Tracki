import datetime
from unittest import mock

import freezegun
import inject
import pytest

from tracki.src.application import use_cases, repositories
from tracki.src.domain import entities


@pytest.fixture()
def shift_repo_mock() -> mock.Mock:
    return mock.Mock(spec_set=repositories.ShiftRepository)


@pytest.fixture(autouse=True)
def di_config(shift_repo_mock: mock.Mock) -> None:
    def di_configuration(binder: inject.Binder) -> None:
        binder.bind(repositories.ShiftRepository, shift_repo_mock)

    inject.clear_and_configure(di_configuration)


def test_should_save_shift_start(shift_repo_mock: mock.Mock) -> None:
    input_dto = use_cases.StartingShiftUseCase.InputDTO(category_id='category1')

    with freezegun.freeze_time('2010-01-01'):
        use_cases.StartingShiftUseCase().execute(input_dto)

    shift_repo_mock.save.assert_called_once_with(
        entities.Shift(
            category_id='category1', start_time=datetime.datetime(2010, 1, 1), id=mock.ANY
        )
    )
