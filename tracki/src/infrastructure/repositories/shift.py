import datetime

from tracki.src.application import repositories
from tracki.src.domain import entities


class FileShiftRepository(repositories.ShiftRepository):

    def __init__(self, file_path: str):
        self._file_path = file_path

    def save(self, shift: entities.Shift) -> None:
        with open(self._file_path, 'a') as f:
            start = self._format_datetime(shift.start_time)
            end = self._format_datetime(shift.end_time)
            f.write(f'{shift.category.name},{start},{end}\n')

    def _format_datetime(self, dt: datetime.datetime) -> str:
        return dt.strftime('%Y-%m-%d %H:%M:%S')
