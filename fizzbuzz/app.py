from typing import Iterable

from fizzbuzz.interface import INumberConsumer


class App:
    def __init__(self, printer: INumberConsumer):
        self.printer = printer

    def run(self, numbers: Iterable[int]):
        for i in numbers:
            self.printer.consume(i)
