from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    accumulator = set()
    for itemA in list1:
        for itemB in list2:
            if not (itemA != itemB):
                accumulator.add(itemA)
    return sorted(accumulator)