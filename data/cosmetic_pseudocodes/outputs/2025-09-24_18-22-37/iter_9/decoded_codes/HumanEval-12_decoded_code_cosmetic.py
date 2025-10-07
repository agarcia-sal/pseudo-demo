from typing import Iterable, Optional, Sized, TypeVar

T = TypeVar('T', bound=Sized)

def longest(original_collection: Iterable[T]) -> Optional[T]:
    # Convert to list for multiple passes and indexing
    items = list(original_collection)
    if not items:
        return None

    temp_max = 0
    for item in items:
        length = len(item)
        if length > temp_max:
            temp_max = length

    for item in items:
        if len(item) == temp_max:
            return item
    return None