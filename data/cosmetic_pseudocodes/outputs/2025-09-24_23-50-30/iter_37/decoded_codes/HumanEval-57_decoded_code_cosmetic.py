from typing import Iterable, TypeVar

T = TypeVar('T')

def monotonic(container: Iterable[T]) -> bool:
    lst = list(container)
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)