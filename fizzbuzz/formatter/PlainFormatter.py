from ..interface import INumberFormatter
from ..utils import implements


@implements(INumberFormatter)
class PlainFormatter:
    def format(self, i: int) -> str:
        return f"{i}"
