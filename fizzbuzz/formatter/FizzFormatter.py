from ..interface import INumberFormatter
from ..utils import implements


@implements(INumberFormatter)
class FizzFormatter:
    def format(self, i: int) -> str:
        return "Fizz"
