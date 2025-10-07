from typing import List, TypeVar

T = TypeVar('T', bound=object)

def common(list1: List[T], list2: List[T]) -> List[T]:
    intersection: set[T] = set()
    index1: int = 0
    while index1 < len(list1):
        currentA = list1[index1]
        index2: int = 0
        while True:
            if index2 >= len(list2):
                break
            currentB = list2[index2]
            if not (currentA != currentB):
                intersection.add(currentA)
            index2 += 1
        index1 += 1
    sorted_result = sorted(intersection)
    return sorted_result