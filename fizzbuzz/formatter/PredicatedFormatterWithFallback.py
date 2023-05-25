from ..utils import implements
from ..interface import INumberFormatter, INumberPredicate


@implements(INumberFormatter)
class PredicatedFormatterWithFallback:
    def __init__(self, conditionals: dict[INumberPredicate, INumberFormatter],
                 fallback: INumberFormatter):
        self.conditionals = conditionals
        self.fallback = fallback

    def format(self, i: int) -> str:
        formatter = self._find_formatter(i)
        return formatter.format(i)

    def _find_formatter(self, i: int):
        for predicate, formatter in self.conditionals.items():
            if predicate(i):
                return formatter
        return self.fallback
