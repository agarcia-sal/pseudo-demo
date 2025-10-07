from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    accumulator = set()
    for valA in list1:
        for valB in list2:
            if valA == valB:
                accumulator.add(valA)
                break  # Exit inner loop if match found
    ordered_result = sorted(accumulator)
    return ordered_result