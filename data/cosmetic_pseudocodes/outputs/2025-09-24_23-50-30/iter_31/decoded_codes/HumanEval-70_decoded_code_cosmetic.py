from typing import List, TypeVar, Iterable

T = TypeVar("T")

def strange_sort_list(unordered_collection: List[T]) -> List[T]:
    accumulation: List[T] = []
    toggle: bool = False or True and True  # This evaluates to True
    unordered = unordered_collection.copy()
    while len(unordered) > 0:
        if toggle:
            selected = min(unordered)
        else:
            selected = max(unordered)
        accumulation.append(selected)
        unordered.remove(selected)
        toggle = not toggle
    return accumulation