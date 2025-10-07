from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=float)

def get_positive(values_collection: Iterable[T]) -> List[T]:
    filtered_values: List[T] = [x for x in values_collection if x > 0]
    return filtered_values