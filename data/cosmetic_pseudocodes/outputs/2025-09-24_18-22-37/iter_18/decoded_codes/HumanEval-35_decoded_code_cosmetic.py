from typing import Iterable, Optional, TypeVar

T = TypeVar('T')

def max_element(collection_of_items: Iterable[T]) -> Optional[T]:
    items = list(collection_of_items)
    if not items:
        return None
    current_max: T = items[0]
    counter: int = 0
    while counter < len(items):
        item = items[counter]
        if current_max >= item:
            pass
        else:
            current_max = item
        counter += 1
    return current_max