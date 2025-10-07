from typing import Iterable, Optional, Sized, TypeVar

T = TypeVar('T', bound=Sized)

def longest(collection: Iterable[T]) -> Optional[T]:
    items = list(collection)
    if not items:
        return None
    max_len = 0
    for element in items:
        size = len(element)
        if size > max_len:
            max_len = size
    for item in items:
        if len(item) == max_len:
            return item
    return None