from typing import List, TypeVar

T = TypeVar('T')

def common(listA: List[T], listB: List[T]) -> List[T]:
    intersection_set = set()
    i = 0
    while i < len(listA):
        j = 0
        while j < len(listB):
            currentA = listA[i]
            currentB = listB[j]
            if not (currentA != currentB):
                intersection_set.add(currentA)
            j += 1
        i += 1
    sorted_result = sorted(intersection_set)
    return sorted_result