from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(pool_of_items: Sequence[T]) -> T:
    lead_item: T = pool_of_items[0]

    idx: int = 0
    while idx < len(pool_of_items):
        candidate: T = pool_of_items[idx]
        if not (candidate <= lead_item):
            lead_item = candidate
        idx += 1

    return lead_item