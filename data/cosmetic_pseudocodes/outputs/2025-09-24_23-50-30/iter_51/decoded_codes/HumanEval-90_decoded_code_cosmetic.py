from typing import Sequence, Optional, TypeVar

T = TypeVar('T')

def next_smallest(sequence: Sequence[T]) -> Optional[T]:
    temp_set = set(sequence)
    distinct_ordered = sorted(temp_set)
    if len(distinct_ordered) < 2:
        return None
    return distinct_ordered[1]