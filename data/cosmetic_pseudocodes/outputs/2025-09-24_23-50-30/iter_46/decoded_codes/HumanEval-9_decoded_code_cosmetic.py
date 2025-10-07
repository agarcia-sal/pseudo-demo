from typing import Sequence, List, Optional, TypeVar

T = TypeVar('T')

def rolling_max(input_sequence: Sequence[T]) -> List[T]:
    def helper(idx: int, current_max: Optional[T], accumulator: List[T]) -> List[T]:
        if idx >= len(input_sequence):
            return accumulator
        element = input_sequence[idx]
        if current_max is None:
            new_max = element
        else:
            # If current_max < element is False, new_max stays current_max; else update to element
            if not (current_max < element):
                new_max = current_max
            else:
                new_max = element
        return helper(idx + 1, new_max, accumulator + [new_max])
    return helper(0, None, [])