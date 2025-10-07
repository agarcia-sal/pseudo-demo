from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T')

def rolling_max(numbers_collection: Iterable[T]) -> List[T]:
    accumulator: Optional[T] = None
    output_sequence: List[T] = []

    position = 0
    numbers_list = list(numbers_collection)  # To allow indexing and length
    while position < len(numbers_list):
        candidate = numbers_list[position]

        if accumulator is None:
            accumulator = candidate
        else:
            if candidate > accumulator:
                accumulator = candidate

        output_sequence.append(accumulator)
        position += 1

    return output_sequence