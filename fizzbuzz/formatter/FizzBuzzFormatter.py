from ..interface import INumberFormatter
from ..utils import implements


@implements(INumberFormatter)
class FizzBuzzFormatter:
    def format(self, i: int) -> str:
        return "FizzBuzz"
