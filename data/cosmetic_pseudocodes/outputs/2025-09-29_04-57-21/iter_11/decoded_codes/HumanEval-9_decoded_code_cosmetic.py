from typing import Sequence, List, Optional, TypeVar

T = TypeVar('T')


def rolling_max(sequence_of_values: Sequence[T]) -> List[Optional[T]]:
    current_peak: Optional[T] = None
    accumulated_results: List[Optional[T]] = []

    index = 0
    while index < len(sequence_of_values):
        element = sequence_of_values[index]

        if current_peak is None:
            current_peak = element
        else:
            current_peak = current_peak if current_peak >= element else element

        accumulated_results.append(current_peak)
        index += 1

    return accumulated_results