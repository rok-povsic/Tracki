import datetime

import freezegun
import pytest

from tracki.src.domain import (
    entities,
    exceptions,
)


@pytest.fixture()
def shift():
    return entities.Shift('A')


def test_shift_not_running_before_starting(shift: entities.Shift):
    assert not shift.is_running


def test_shift_running_after_starting(shift: entities.Shift):
    shift.start()
    assert shift.is_running


def test_shift_not_running_after_ending(shift: entities.Shift):
    shift.start()
    shift.end()
    assert not shift.is_running


def test_shift_times_not_set_before_starting(shift: entities.Shift):
    assert not shift.start_time
    assert not shift.end_time


def test_shift_times_correct_after_starting(shift: entities.Shift):
    with freezegun.freeze_time('2010-01-01 12:00'):
        shift.start()
    assert shift.start_time == datetime.datetime(2010, 1, 1, 12, 0)
    assert not shift.end_time


def test_shift_times_correct_after_ending(shift: entities.Shift):
    with freezegun.freeze_time('2010-01-01 12:00'):
        shift.start()
    with freezegun.freeze_time('2010-01-02 12:01'):
        shift.end()
    assert shift.start_time == datetime.datetime(2010, 1, 1, 12, 0)
    assert shift.end_time == datetime.datetime(2010, 1, 2, 12, 1)


def test_raise_shift_already_started(shift: entities.Shift):
    shift.start()
    with pytest.raises(exceptions.ShiftAlreadyStartedException):
        shift.start()


def test_raise_shift_already_ended(shift: entities.Shift):
    shift.start()
    shift.end()
    with pytest.raises(exceptions.ShiftAlreadyEndedException):
        shift.end()


def test_raise_shift_not_yet_started(shift: entities.Shift):
    with pytest.raises(exceptions.ShiftNotYetStartedException):
        shift.end()