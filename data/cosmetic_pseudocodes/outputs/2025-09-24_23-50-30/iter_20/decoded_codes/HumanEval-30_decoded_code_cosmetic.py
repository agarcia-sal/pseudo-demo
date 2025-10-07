from typing import Iterable, List, TypeVar

T = TypeVar("T", bound=float)  # Assuming numeric types compatible with <= 0

def get_positive(collection_of_values: Iterable[T]) -> List[T]:
    accumulator: List[T] = []
    for each_item in collection_of_values:
        if not (each_item <= 0):
            accumulator.append(each_item)
    return accumulator