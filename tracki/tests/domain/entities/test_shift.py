import datetime

import freezegun
import pytest

from tracki.src.domain.entities import Shift


@pytest.fixture()
def shift():
    return Shift('A')


def test_shift_not_running_before_starting(shift):
    assert not shift.is_running


def test_shift_running_after_starting(shift):
    shift.start()
    assert shift.is_running


def test_shift_not_running_after_ending(shift):
    shift.start()
    shift.end()
    assert not shift.is_running


def test_shift_times_not_set_before_starting(shift):
    assert not shift.start_time
    assert not shift.end_time


def test_shift_times_correct_after_starting(shift):
    with freezegun.freeze_time('2010-01-01 12:00'):
        shift.start()
    assert shift.start_time == datetime.datetime(2010, 1, 1, 12, 0)
    assert not shift.end_time


def test_shift_times_correct_after_ending(shift):
    with freezegun.freeze_time('2010-01-01 12:00'):
        shift.start()
    with freezegun.freeze_time('2010-01-02 12:01'):
        shift.end()
    assert shift.start_time == datetime.datetime(2010, 1, 1, 12, 0)
    assert shift.end_time == datetime.datetime(2010, 1, 2, 12, 1)
