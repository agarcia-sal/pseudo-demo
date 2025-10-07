from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T')


def rolling_max(sequence_values: Iterable[T]) -> List[T]:
    accumulator: Optional[T] = None
    output_collection: List[T] = []
    idx = 0
    values = list(sequence_values)  # To support indexing by idx

    while idx < len(values):
        current_element = values[idx]

        if accumulator is not None:
            temp_max = accumulator
            if current_element > temp_max:
                accumulator = current_element
        else:
            accumulator = current_element

        output_collection.append(accumulator)
        idx += 1

    return output_collection