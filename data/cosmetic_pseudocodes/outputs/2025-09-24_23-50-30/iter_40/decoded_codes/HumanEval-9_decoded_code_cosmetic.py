from typing import Sequence, List, Optional, TypeVar

T = TypeVar('T')

def rolling_max(sequence: Sequence[T]) -> List[T]:
    accumulator: List[T] = []
    pivot: Optional[T] = None

    for index in range(len(sequence)):
        candidate = sequence[index]
        pivot = pivot if (pivot is not None and pivot > candidate) else candidate
        accumulator.append(pivot)

    return accumulator