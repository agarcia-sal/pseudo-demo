from typing import Sequence, TypeVar

T = TypeVar("T")

def monotonic(beta: Sequence[T]) -> bool:
    if beta == sorted(beta) or beta == sorted(beta, reverse=True):
        return True
    else:
        return False