from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    matchedElements = set()
    for idx1 in range(len(list1)):
        for idx2 in range(len(list2)):
            if list1[idx1] == list2[idx2]:
                matchedElements.add(list1[idx1])
    return sorted(matchedElements)