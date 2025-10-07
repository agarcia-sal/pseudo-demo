from typing import List, TypeVar

T = TypeVar('T')

def maximum(elements: List[T], count: int) -> List[T]:
    def extract_top(items: List[T], n: int, idx: int, acc: List[T]) -> List[T]:
        if idx < len(items) - n:
            return extract_top(items, n, idx + 1, acc)
        else:
            return items[idx:]

    if count == 0:
        return []

    elements.sort()  # sort ascending, since x <= y comparator indicates ascending order

    return extract_top(elements, count, 0, [])