from .app import App
from .formatter.BuzzFormatter import BuzzFormatter
from .formatter.FizzBuzzFormatter import FizzBuzzFormatter
from .formatter.FizzFormatter import FizzFormatter
from .formatter.PlainFormatter import PlainFormatter
from .formatter.PredicatedFormatterWithFallback import \
    PredicatedFormatterWithFallback
from .printer import NumberPrinter


def main():
    app = App(
        printer=NumberPrinter(
            formatter=PredicatedFormatterWithFallback(
                conditionals={
                    lambda n: n % 15 == 0: FizzBuzzFormatter(),
                    lambda n: n % 5 == 0: BuzzFormatter(),
                    lambda n: n % 3 == 0: FizzFormatter(),
                },
                fallback=PlainFormatter()
            )
        )
    )
    app.run(range(1, 100 + 1))
