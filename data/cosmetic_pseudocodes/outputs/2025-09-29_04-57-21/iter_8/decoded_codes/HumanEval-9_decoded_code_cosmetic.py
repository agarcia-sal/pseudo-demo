from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T')


def rolling_max(sequence: Iterable[T]) -> List[T]:
    current_peak: Optional[T] = None
    outcomes: List[T] = []

    for item in sequence:
        if current_peak is None or current_peak < item:
            current_peak = item
        outcomes.append(current_peak)

    return outcomes