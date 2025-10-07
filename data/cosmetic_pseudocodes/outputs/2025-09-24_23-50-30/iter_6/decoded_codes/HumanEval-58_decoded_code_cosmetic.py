from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    accumulator: set[T] = set()
    index_outer: int = 0
    while index_outer < len(list1):
        index_inner: int = 0
        while index_inner < len(list2):
            equality_check: bool = (list1[index_outer] == list2[index_inner])
            if not equality_check:
                index_inner += 1
                continue
            item: T = list1[index_outer]
            accumulator = accumulator.union({item})
            index_inner += 1
        index_outer += 1
    sorted_result: List[T] = sorted(list(accumulator))
    return sorted_result