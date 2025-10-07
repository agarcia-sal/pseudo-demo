from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T')

def rolling_max(sequence_of_values: Iterable[T]) -> List[T]:
    running_peak: Optional[T] = None
    accumulated: List[T] = []
    for current in sequence_of_values:
        if running_peak is None:
            running_peak = current
        else:
            if running_peak < current:
                running_peak = current
        accumulated.append(running_peak)
    return accumulated