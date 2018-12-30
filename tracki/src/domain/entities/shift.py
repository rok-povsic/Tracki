import datetime
import typing
import uuid

import attr


@attr.s
class Shift:
    category_id: str = attr.ib()
    start_time: typing.Optional[datetime.datetime] = attr.ib(default=None)
    end_time: typing.Optional[datetime.datetime] = attr.ib(default=None)
    id: uuid.UUID = attr.ib(factory=lambda: uuid.uuid4)

    def start(self) -> None:
        self.start_time = datetime.datetime.now()

    def end(self) -> None:
        self.end_time = datetime.datetime.now()

    @property
    def is_running(self) -> bool:
        return bool(self.start_time) and not bool(self.end_time)
