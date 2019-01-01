from unittest import mock

import inject
import pytest

from tracki.src.application import repositories


@pytest.fixture()
def shift_repo_mock() -> mock.Mock:
    return mock.Mock(spec_set=repositories.ShiftRepository)


@pytest.fixture(autouse=True)
def di_config(shift_repo_mock: mock.Mock) -> None:
    def di_configuration(binder: inject.Binder) -> None:
        binder.bind(repositories.ShiftRepository, shift_repo_mock)

    inject.clear_and_configure(di_configuration)
