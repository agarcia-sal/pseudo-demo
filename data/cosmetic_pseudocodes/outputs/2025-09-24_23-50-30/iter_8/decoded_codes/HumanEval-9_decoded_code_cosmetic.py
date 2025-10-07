from typing import Sequence, List, TypeVar, Optional

T = TypeVar('T')

def rolling_max(sequence_container: Sequence[T]) -> List[T]:
    accumulator: List[T] = []
    peak_value: Optional[T] = None
    for index_counter, current_element in enumerate(sequence_container):
        if peak_value is None:
            peak_value = current_element
        elif peak_value < current_element:
            peak_value = current_element
        accumulator.append(peak_value)
    return accumulator