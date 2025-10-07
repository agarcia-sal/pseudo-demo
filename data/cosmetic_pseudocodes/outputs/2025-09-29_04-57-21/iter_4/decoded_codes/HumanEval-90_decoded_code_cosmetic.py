from typing import List, Optional, TypeVar

T = TypeVar('T')

def next_smallest(array_of_values: List[T]) -> Optional[T]:
    distinct_ordered = sorted(set(array_of_values))
    if len(distinct_ordered) < 2:
        return None
    return distinct_ordered[1]