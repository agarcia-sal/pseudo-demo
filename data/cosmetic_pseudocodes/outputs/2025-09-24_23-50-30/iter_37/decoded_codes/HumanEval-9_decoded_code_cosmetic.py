from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T')

def rolling_max(sequence_of_values: Iterable[T]) -> List[T]:
    current_peak: Optional[T] = None
    accumulating_result: List[T] = []

    for element in sequence_of_values:
        if current_peak is None:
            current_peak = element
        else:
            if element > current_peak:
                current_peak = element
        accumulating_result.append(current_peak)

    return accumulating_result