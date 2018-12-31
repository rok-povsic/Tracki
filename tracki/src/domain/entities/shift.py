import datetime
import typing
import uuid

import attr

from tracki.src.domain import exceptions


@attr.s
class Shift:
    category_id: str = attr.ib()
    start_time: typing.Optional[datetime.datetime] = attr.ib(default=None)
    end_time: typing.Optional[datetime.datetime] = attr.ib(default=None)
    id: uuid.UUID = attr.ib(factory=lambda: uuid.uuid4)

    def start(self) -> None:
        if self.start_time:
            raise exceptions.ShiftAlreadyStartedException
        self.start_time = datetime.datetime.now()

    def end(self) -> None:
        if not self.start_time:
            raise exceptions.ShiftNotYetStartedException
        if self.end_time:
            raise exceptions.ShiftAlreadyEndedException
        self.end_time = datetime.datetime.now()

    @property
    def is_running(self) -> bool:
        return bool(self.start_time) and not bool(self.end_time)
