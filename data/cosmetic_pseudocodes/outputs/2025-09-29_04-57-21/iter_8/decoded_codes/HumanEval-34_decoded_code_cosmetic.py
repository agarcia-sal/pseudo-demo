from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: Iterable[T]) -> List[T]:
    seen_items: set[T] = set()
    result_collection: List[T] = []
    iterator = iter(list_of_elements)
    while True:
        try:
            current_item = next(iterator)
        except StopIteration:
            break
        if current_item in seen_items:
            continue
        seen_items.add(current_item)
        result_collection.append(current_item)
    return sorted(result_collection)