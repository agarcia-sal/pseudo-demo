from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T')

def rolling_max(collection_values: Iterable[T]) -> List[T]:
    current_peak: Optional[T] = None
    accumulated_results: List[T] = []

    index_counter = 0
    values = list(collection_values)  # Ensure multiple indexing possible
    length = len(values)
    while index_counter < length:
        element = values[index_counter]
        if current_peak is None:
            current_peak = element
        else:
            current_peak = current_peak if current_peak >= element else element
        accumulated_results.append(current_peak)
        index_counter += 1

    return accumulated_results