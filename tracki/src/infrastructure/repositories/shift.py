import datetime
import os
import typing

from tracki.src.application import repositories
from tracki.src.domain import entities
from tracki.src.infrastructure.exceptions import shift as exceptions


DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class FileShiftRepository(repositories.ShiftRepository):

    def __init__(self, file_path: str):
        self._file_path = file_path

    def save(self, shift: entities.Shift) -> None:
        shifts = self._read_shifts()
        if shifts and shifts[-1].is_running:
            shifts = shifts[:-1]
        shifts.append(shift)
        self._write_shifts(shifts)

    def get_last(self) -> entities.Shift:
        shifts = self._read_shifts()
        if not shifts:
            raise exceptions.NoShiftsPresentException
        return shifts[-1]

    def _write_shifts(self, shifts: typing.List[entities.Shift]) -> None:
        with open(self._file_path, 'w') as data_file:
            for shift in shifts:
                start = self._format_datetime(shift.start_time)
                end = self._format_datetime(shift.end_time)
                data_file.write(f'{shift.category.name},{start},{end}\n')

    def _format_datetime(self, timestamp: typing.Optional[datetime.datetime]) -> str:
        if not timestamp:
            return 'null'
        return timestamp.strftime(DATETIME_FORMAT)

    def _read_shifts(self) -> typing.List[entities.Shift]:
        if not os.path.exists(self._file_path):
            return []

        with open(self._file_path) as data_file:
            lines = [l for l in data_file.readlines() if l.strip()]

        shifts = []
        for line in lines:
            shift = self._line_to_shift(line)
            shifts.append(shift)
        return shifts

    def _line_to_shift(self, line: str) -> entities.Shift:
        parts = line.strip().split(',')
        category_name = parts[0]
        start = datetime.datetime.strptime(parts[1], DATETIME_FORMAT)
        end = datetime.datetime.strptime(parts[2], DATETIME_FORMAT) if parts[2] != 'null' else None
        return entities.Shift(
            category=entities.Category(name=category_name), start_time=start, end_time=end
        )
