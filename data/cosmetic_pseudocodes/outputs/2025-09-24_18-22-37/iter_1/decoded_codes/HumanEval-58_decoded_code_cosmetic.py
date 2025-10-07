from typing import List, TypeVar

T = TypeVar("T")

def common(list1: List[T], list2: List[T]) -> List[T]:
    matched_elements = set()
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                matched_elements.add(list1[i])
    return sorted(matched_elements)