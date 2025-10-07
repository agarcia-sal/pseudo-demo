from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    matched_elements: set[T] = set()
    index_one: int = 0
    while index_one < len(list1):
        val1: T = list1[index_one]
        index_two: int = 0
        while index_two < len(list2):
            if val1 == list2[index_two]:
                matched_elements.add(val1)
            index_two += 1
        index_one += 1
    output_list: List[T] = list(matched_elements)
    output_list.sort()
    return output_list