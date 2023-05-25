from ..interface import INumberFormatter
from ..utils import implements


@implements(INumberFormatter)
class BuzzFormatter:
    def format(self, i: int) -> str:
        return "Buzz"
