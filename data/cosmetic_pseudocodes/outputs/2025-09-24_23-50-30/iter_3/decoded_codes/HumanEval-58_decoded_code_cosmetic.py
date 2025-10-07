from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    intersected: set[T] = set()
    i: int = 0
    while i < len(list1):
        j: int = 0
        while j < len(list2):
            if list1[i] == list2[j]:
                intersected.add(list1[i])
            j += 1
        i += 1
    return sorted(intersected)