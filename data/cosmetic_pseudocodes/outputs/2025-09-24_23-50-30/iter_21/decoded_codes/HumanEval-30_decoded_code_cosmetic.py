from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=float)

def get_positive(input_collection: Iterable[T]) -> List[T]:
    return [individual_item for individual_item in input_collection if individual_item > 0]