from typing import Sequence, List, Optional, TypeVar

T = TypeVar('T', bound='SupportsLessThanOrEqual')

from typing import Protocol

class SupportsLessThanOrEqual(Protocol):
    def __le__(self: T, other: T) -> bool: ...

def rolling_max(sequence_of_values: Sequence[T]) -> List[Optional[T]]:
    accumulator: List[Optional[T]] = []
    current_peak: Optional[T] = None
    index = 0

    while index < len(sequence_of_values):
        candidate = sequence_of_values[index]
        if current_peak is None:
            current_peak = candidate
        else:
            if not candidate <= current_peak:
                current_peak = candidate
        accumulator.append(current_peak)
        index += 1

    return accumulator