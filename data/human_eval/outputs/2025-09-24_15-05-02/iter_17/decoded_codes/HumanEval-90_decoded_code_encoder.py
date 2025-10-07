from typing import List, Optional, TypeVar

T = TypeVar('T')

def next_smallest(lst: List[T]) -> Optional[T]:
    sorted_unique = sorted(set(lst))
    if len(sorted_unique) < 2:
        return None
    else:
        return sorted_unique[1]