from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThan')

def monotonic(arr: Sequence[T]) -> bool:
    return arr == sorted(arr) or arr == sorted(arr, reverse=True)