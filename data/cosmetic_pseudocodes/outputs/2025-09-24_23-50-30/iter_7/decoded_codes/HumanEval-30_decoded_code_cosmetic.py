from typing import Iterable, List, TypeVar

T = TypeVar("T", bound=float)

def get_positive(elements_collection: Iterable[T]) -> List[T]:
    filtered_values: List[T] = []
    for single_value in elements_collection:
        if not (single_value <= 0):
            filtered_values.append(single_value)
    return filtered_values