import uuid

import attr


@attr.s
class Category:
    id: uuid.UUID = attr.ib()
    name: str = attr.ib()
