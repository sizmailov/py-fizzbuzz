from typing import Protocol, runtime_checkable


@runtime_checkable
class INumberFormatter(Protocol):
    def format(self, i: int) -> str:
        ...


@runtime_checkable
class INumberPredicate(Protocol):
    def __call__(self, i: int) -> bool:
        ...


@runtime_checkable
class INumberConsumer(Protocol):
    def consume(self, i: int) -> str:
        ...
