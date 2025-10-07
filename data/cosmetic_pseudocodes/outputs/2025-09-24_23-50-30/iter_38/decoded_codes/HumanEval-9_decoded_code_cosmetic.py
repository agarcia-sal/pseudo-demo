from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T')

def rolling_max(sequence_of_values: Iterable[T]) -> List[T]:
    accumulator: Optional[T] = None
    output_collection: List[T] = []

    index_counter = 0
    sequence_list = list(sequence_of_values)  # support multiple passes and indexing
    length = len(sequence_list)

    while index_counter < length:
        current_element = sequence_list[index_counter]

        if accumulator is None:
            accumulator = current_element
        else:
            if accumulator >= current_element:
                accumulator = accumulator
            else:
                accumulator = current_element

        output_collection.append(accumulator)
        index_counter += 1

    return output_collection