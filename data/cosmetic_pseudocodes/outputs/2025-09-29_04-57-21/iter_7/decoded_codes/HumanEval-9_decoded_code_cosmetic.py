from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T')

def rolling_max(sequence_of_values: Iterable[T]) -> List[T]:
    current_peak: Optional[T] = None
    accumulated_results: List[T] = []

    iterator_position = 0
    values_list = list(sequence_of_values)  # Ensure indexing and multiple passes if needed
    length = len(values_list)
    while iterator_position < length:
        element = values_list[iterator_position]

        if current_peak is None:
            current_peak = element
        else:
            if element > current_peak:
                current_peak = element

        accumulated_results.append(current_peak)
        iterator_position += 1

    return accumulated_results