from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __ge__(self: T, other: T) -> bool:
        ...

def rolling_max(sequence_of_values: Iterable[T]) -> List[T]:
    index_counter: int = 0
    current_peak: Optional[T] = None
    accumulated_results: List[T] = []
    sequence_list = list(sequence_of_values)  # Convert to list for indexing

    while True:
        if index_counter < len(sequence_list):
            current_entry = sequence_list[index_counter]
            if current_peak is not None:
                current_peak = current_peak if current_peak >= current_entry else current_entry
            else:
                current_peak = current_entry
            accumulated_results.append(current_peak)
            index_counter += 1
        else:
            break

    return accumulated_results