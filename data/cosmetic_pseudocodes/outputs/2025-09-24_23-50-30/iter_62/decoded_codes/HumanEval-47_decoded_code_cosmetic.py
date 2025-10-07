from typing import Sequence, Union, List, TypeVar

T = TypeVar('T', int, float)
Number = Union[int, float]

def median(collection: Sequence[T]) -> float:
    def median_helper(sequence: Sequence[T]) -> float:
        n = len(sequence)
        mid = n // 2
        if n % 2 == 1:
            return float(sequence[mid])
        else:
            return (sequence[mid - 1] + sequence[mid]) / 2.0

    sorted_seq: List[T] = sorted(collection)
    return median_helper(sorted_seq)