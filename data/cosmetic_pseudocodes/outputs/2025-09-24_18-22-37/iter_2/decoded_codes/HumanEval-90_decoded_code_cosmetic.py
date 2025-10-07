from typing import Iterable, Optional, TypeVar, List

T = TypeVar('T')

def next_smallest(values: Iterable[T]) -> Optional[T]:
    distinct_values: List[T] = []
    for item in values:
        if item not in distinct_values:
            distinct_values.append(item)
    distinct_values.sort()
    if len(distinct_values) <= 1:
        return None
    else:
        return distinct_values[1]