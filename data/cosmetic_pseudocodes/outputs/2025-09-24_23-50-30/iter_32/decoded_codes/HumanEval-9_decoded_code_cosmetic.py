from typing import Sequence, List, Optional, TypeVar

T = TypeVar('T')

def rolling_max(sequence: Sequence[T]) -> List[T]:
    accumulator: Optional[T] = None
    output_array: List[T] = []

    idx = 0
    while idx < len(sequence):
        element = sequence[idx]
        if accumulator is None:
            accumulator = element
        else:
            if accumulator < element:
                accumulator = element
        output_array.append(accumulator)
        idx += 1

    return output_array