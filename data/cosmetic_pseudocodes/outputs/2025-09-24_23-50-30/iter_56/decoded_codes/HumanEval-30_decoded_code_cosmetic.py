from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=float)

def get_positive(batch_of_items: Iterable[T]) -> List[T]:
    return [datum for datum in batch_of_items if datum > 0]