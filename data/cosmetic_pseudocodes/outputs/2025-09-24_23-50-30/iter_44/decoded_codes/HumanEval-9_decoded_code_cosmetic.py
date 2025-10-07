from typing import Sequence, List, Optional, TypeVar

T = TypeVar('T', bound='Comparable')

# A Protocol is not strictly necessary since comparison operators are built in but can be done for clarity.
# Defining a Comparable protocol would require importing typing_extensions for Python < 3.8,
# Here we just assume T supports > comparison.

def rolling_max(sequence: Sequence[T]) -> List[T]:
    def helper(index: int, current_peak: Optional[T], accumulator: List[T]) -> List[T]:
        if index >= len(sequence):
            return accumulator
        element = sequence[index]
        updated_peak = element if current_peak is None or element > current_peak else current_peak
        return helper(index + 1, updated_peak, accumulator + [updated_peak])
    return helper(0, None, [])