from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    # Accumulate items from list1 that appear in list2 without duplicates
    acc: List[T] = []
    for currentItem in list1:
        if currentItem not in acc and any(item == currentItem for item in list2):
            acc.append(currentItem)
    return sorted(acc)