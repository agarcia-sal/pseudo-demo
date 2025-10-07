from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound='SupportsFloat')

class SupportsFloat:
    def __float__(self) -> float:
        ...

def median(elements_collection: Sequence[T]) -> float:
    sorted_sequence = sorted(elements_collection)
    size_count = len(sorted_sequence)
    half_idx = size_count // 2
    if size_count % 2 != 0:
        return float(sorted_sequence[half_idx])
    return (float(sorted_sequence[half_idx - 1]) + float(sorted_sequence[half_idx])) / 2.0