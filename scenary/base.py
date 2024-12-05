from typing import Protocol


class BaseScenary(Protocol):

    def make_step(self):
        raise NotImplementedError

    def __bool__(self):
        return True
