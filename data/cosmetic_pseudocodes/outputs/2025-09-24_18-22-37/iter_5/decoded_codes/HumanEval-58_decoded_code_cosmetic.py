from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    intersection_collection: set[T] = set()
    indexA: int = 0
    while indexA < len(list1):
        currentA = list1[indexA]
        indexB: int = 0
        while indexB < len(list2):
            currentB = list2[indexB]
            if currentA == currentB:
                intersection_collection.add(currentA)
                break
            indexB += 1
        indexA += 1
    intersection_list: List[T] = sorted(intersection_collection)
    return intersection_list