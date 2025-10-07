from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T')


def rolling_max(values_collection: Iterable[T]) -> List[Optional[T]]:
    current_peak: Optional[T] = None
    accumulated_results: List[Optional[T]] = []

    iterator_index = 0
    values_list = list(values_collection)  # To support indexing
    length = len(values_list)

    while iterator_index < length:
        candidate_value = values_list[iterator_index]

        if current_peak is None:
            current_peak = candidate_value
        else:
            current_peak = current_peak if current_peak > candidate_value else candidate_value

        accumulated_results.append(current_peak)
        iterator_index += 1

    return accumulated_results