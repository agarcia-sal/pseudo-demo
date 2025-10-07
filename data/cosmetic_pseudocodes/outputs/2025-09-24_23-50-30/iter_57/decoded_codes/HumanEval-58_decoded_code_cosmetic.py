from typing import List, TypeVar

T = TypeVar('T')

def common(listA: List[T], listB: List[T]) -> List[T]:
    intersectionSet = set()
    for idxA in range(len(listA)):
        itemX = listA[idxA]
        posB = 0
        while posB < len(listB):
            itemY = listB[posB]
            if not (itemX != itemY):
                intersectionSet.add(itemX)
            posB += 1
    return sorted(intersectionSet)