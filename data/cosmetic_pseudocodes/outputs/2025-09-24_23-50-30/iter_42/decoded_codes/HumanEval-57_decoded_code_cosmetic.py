from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThan')

def monotonic(sequence: Sequence[T]) -> bool:
    arr1 = sorted(sequence)
    arr2 = sorted(sequence, reverse=True)
    if sequence == arr1:
        return True
    if sequence == arr2:
        return True
    return False