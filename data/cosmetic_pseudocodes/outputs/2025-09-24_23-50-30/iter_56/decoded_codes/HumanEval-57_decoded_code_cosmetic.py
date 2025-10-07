from typing import Sequence, TypeVar

T = TypeVar("T")

def monotonic(identifier_one: Sequence[T]) -> bool:
    return identifier_one == sorted(identifier_one) or identifier_one == sorted(identifier_one, reverse=True)