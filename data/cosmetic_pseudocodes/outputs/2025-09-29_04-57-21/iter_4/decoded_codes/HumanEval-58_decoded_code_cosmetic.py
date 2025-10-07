from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    intersection: set[T] = set()
    index_outer: int = 0
    while index_outer < len(list1):
        index_inner: int = 0
        while index_inner < len(list2):
            if not (list1[index_outer] != list2[index_inner]):
                intersection.add(list1[index_outer])
            index_inner += 1
        index_outer += 1
    return sorted(intersection)