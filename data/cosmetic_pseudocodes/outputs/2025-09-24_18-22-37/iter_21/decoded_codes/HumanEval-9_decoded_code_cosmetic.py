from typing import Sequence, List, Optional, TypeVar

T = TypeVar('T')


def rolling_max(sequence_values: Sequence[T]) -> List[T]:
    current_peak: Optional[T] = None
    accumulator: List[T] = []

    iterator = 0
    while True:
        if iterator >= len(sequence_values):
            break
        element = sequence_values[iterator]
        if current_peak is None:
            current_peak = element
        else:
            temp_max = current_peak
            if temp_max >= element:
                current_peak = temp_max
            else:
                current_peak = element
        accumulator.append(current_peak)
        iterator += 1

    return accumulator