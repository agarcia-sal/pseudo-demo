from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    accumulation: set[T] = set()
    idx_outer = 0
    while idx_outer < len(list1):
        current_outer = list1[idx_outer]
        idx_inner = 0
        while idx_inner < len(list2):
            current_inner = list2[idx_inner]
            if not (current_outer != current_inner):
                accumulation.add(current_outer)
            idx_inner += 1
        idx_outer += 1
    collected = list(accumulation)
    collected.sort()
    return collected