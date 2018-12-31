import datetime
import os

from tracki.src.domain import entities
from tracki.src.infrastructure import repositories


def test_completed_shift_should_be_saved(tmp_path: str) -> None:
    file_path = os.path.join(tmp_path, 'aa.txt')
    shift_repo = repositories.FileShiftRepository(file_path)

    shift_repo.save(
        entities.Shift(
            category=entities.Category(name='AA'),
            start_time=datetime.datetime(2010, 1, 1),
            end_time=datetime.datetime(2010, 1, 1, 0, 5, 0),
        )
    )

    with open(file_path) as data_file:
        file_text = data_file.read()
    assert file_text == 'AA,2010-01-01 00:00:00,2010-01-01 00:05:00\n'
