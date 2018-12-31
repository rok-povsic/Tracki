import datetime
import typing

from tracki.src.application import repositories
from tracki.src.domain import entities


class FileShiftRepository(repositories.ShiftRepository):

    def __init__(self, file_path: str):
        self._file_path = file_path

    def save(self, shift: entities.Shift) -> None:
        with open(self._file_path, 'a') as data_file:
            start = self._format_datetime(shift.start_time)
            end = self._format_datetime(shift.end_time)
            data_file.write(f'{shift.category.name},{start},{end}\n')

    def _format_datetime(self, timestamp: typing.Optional[datetime.datetime]) -> str:
        if not timestamp:
            return 'null'
        return timestamp.strftime('%Y-%m-%d %H:%M:%S')
