from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T')

def rolling_max(sequence_of_values: Iterable[T]) -> List[T]:
    accumulator: Optional[T] = None
    output_collection: List[T] = []

    for value in sequence_of_values:
        if accumulator is None:
            accumulator = value
        else:
            accumulator = accumulator if accumulator >= value else value
        output_collection.append(accumulator)

    return output_collection