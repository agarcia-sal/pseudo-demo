from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    result_set = set()
    for element1 in list1:
        for element2 in list2:
            if element1 == element2:
                result_set.add(element1)
    return sorted(result_set)