from typing import List, TypeVar, Iterable

T = TypeVar('T')

def strange_sort_list(collection: List[T]) -> List[T]:
    outcome: List[T] = []
    toggle: bool = False
    items = collection.copy()
    while items:
        toggle = not toggle
        target = min(items) if toggle else max(items)
        outcome.append(target)
        items.remove(target)
    return outcome