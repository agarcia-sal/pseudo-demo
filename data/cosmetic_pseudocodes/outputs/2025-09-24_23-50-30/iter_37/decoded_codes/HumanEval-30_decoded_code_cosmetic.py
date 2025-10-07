from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=float)

def get_positive(container_of_values: Iterable[T]) -> List[T]:
    return [item for item in container_of_values if not (item <= 0)]