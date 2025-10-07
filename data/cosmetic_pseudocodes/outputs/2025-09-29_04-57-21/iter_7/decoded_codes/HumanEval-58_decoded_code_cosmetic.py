from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    shared_elements = set()
    i = 0
    while i < len(list1):
        j = 0
        while j < len(list2):
            if not (list1[i] != list2[j]):
                shared_elements.add(list1[i])
            j += 1
        i += 1
    return sorted(shared_elements)