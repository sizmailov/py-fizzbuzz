from typing import TypeVar, Type

Class_ = TypeVar("Class_", bound=Type)


def implements(protocol: Type):
    def check(class_: Class_) -> Class_:
        assert issubclass(class_, protocol)
        return class_

    return check
