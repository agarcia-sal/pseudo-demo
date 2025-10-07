from typing import List, Optional, TypeVar

T = TypeVar('T')


def next_smallest(lst: List[T]) -> Optional[T]:
    unique_items = set(lst)
    if len(unique_items) <= 1:
        return None
    temp: List[T] = list(unique_items)
    # Sort temp using a simple selection sort to match pseudocode logic
    for i in range(len(temp) - 1):
        for j in range(i + 1, len(temp)):
            if temp[i] > temp[j]:
                temp[i], temp[j] = temp[j], temp[i]
    return temp[1]