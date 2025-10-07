from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T')

def rolling_max(sequence_of_values: Iterable[T]) -> List[T]:
    accumulator: Optional[T] = None
    outcome: List[T] = []

    iterator_index = 0
    values = list(sequence_of_values)  # Indexable
    length = len(values)
    while iterator_index < length:
        current_element = values[iterator_index]
        if accumulator is None:
            accumulator = current_element
        else:
            temp_max = accumulator
            candidate = current_element
            if candidate > temp_max:
                accumulator = candidate
            else:
                accumulator = temp_max
        outcome.append(accumulator)
        iterator_index += 1

    return outcome