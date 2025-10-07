from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound='SupportsMedian')

class SupportsMedian:
    def __add__(self, other: 'SupportsMedian') -> 'SupportsMedian':
        ...

    def __mul__(self, other: float) -> 'SupportsMedian':
        ...

def median(elements_collection: Sequence[T]) -> Union[T, float]:
    sorted_copy = sorted(elements_collection)
    size_val = len(sorted_copy)
    half_idx = size_val // 2
    if size_val % 2 != 0:
        return sorted_copy[half_idx]
    else:
        left_val = sorted_copy[half_idx - 1]
        right_val = sorted_copy[half_idx]
        sum_vals = left_val + right_val
        avg_val = sum_vals * 0.5
        return avg_val