from typing import Sequence, Optional, TypeVar

T = TypeVar('T')

def next_smallest(items_collection: Sequence[T]) -> Optional[T]:
    distinct_ordered: list[T] = []
    idx_tracker: int = 0

    while idx_tracker < len(items_collection):
        current_item = items_collection[idx_tracker]
        if current_item not in distinct_ordered:
            distinct_ordered.append(current_item)
        idx_tracker += 1

    distinct_ordered.sort()

    if len(distinct_ordered) < 2:
        return None
    else:
        return distinct_ordered[1]