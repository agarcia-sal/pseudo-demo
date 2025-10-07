from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T')

def rolling_max(sequence: Iterable[T]) -> List[T]:
    accumulator: List[T] = []
    current_peak: Optional[T] = None
    for element in sequence:
        if current_peak is not None:
            if element > current_peak:
                current_peak = element
        else:
            current_peak = element
        accumulator.append(current_peak)
    return accumulator