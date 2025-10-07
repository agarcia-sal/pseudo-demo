from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    result_set: set[T] = set()
    for element in list1:
        for item in list2:
            if element == item:
                result_set.add(element)
    result_list: List[T] = sorted(result_set)
    return result_list