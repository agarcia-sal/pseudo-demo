from typing import Iterable, Optional, TypeVar, List, Set

T = TypeVar('T')

def next_smallest(items: Iterable[T]) -> Optional[T]:
    distinct_ordered: List[T] = []
    seen: Set[T] = set()
    for element in items:
        if element not in seen:
            distinct_ordered.append(element)
            seen.add(element)
    ordered_unique = distinct_ordered
    ordered_unique.sort()
    if len(ordered_unique) < 2:
        return None
    else:
        return ordered_unique[1]