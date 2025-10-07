from typing import Iterable, List, Optional, TypeVar

T = TypeVar("T")


def rolling_max(sequence: Iterable[T]) -> List[T]:
    accumulator: Optional[T] = None
    output_collection: List[T] = []

    for element in sequence:
        if accumulator is None:
            accumulator = element
        else:
            accumulator = accumulator if accumulator > element else element
        output_collection.append(accumulator)

    return output_collection