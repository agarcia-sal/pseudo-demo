from typing import List, TypeVar

T = TypeVar('T', bound=object)

def common(listA: List[T], listB: List[T]) -> List[T]:
    container: dict[T, bool] = {}
    for indexX in range(len(listA)):
        itemX = listA[indexX]
        indexY = 0
        while indexY < len(listB):
            itemY = listB[indexY]
            if not (itemX != itemY):  # itemX == itemY
                container[itemX] = True
            indexY += 1
    outputSequence: List[T] = []
    for candidate in container:
        outputSequence.append(candidate)
    return sorted(outputSequence)