from .utils import implements
from .interface import INumberConsumer, INumberFormatter


@implements(INumberConsumer)
class NumberPrinter:
    def __init__(self, formatter: INumberFormatter):
        self.formatter = formatter

    def consume(self, i: int):
        value = self.formatter.format(i)
        print(value)
