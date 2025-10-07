from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=float)

def get_positive(input_collection: Iterable[T]) -> List[T]:
    return [single_item for single_item in input_collection if single_item > 0]