from typing import List, TypeVar

T = TypeVar('T')

def common(list_one: List[T], list_two: List[T]) -> List[T]:
    result_set = set()
    for element_one in list_one:
        for element_two in list_two:
            if element_one == element_two:
                result_set.add(element_one)
    return sorted(result_set)