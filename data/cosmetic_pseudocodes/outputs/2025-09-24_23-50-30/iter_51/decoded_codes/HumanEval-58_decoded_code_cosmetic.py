from typing import Iterable, List, Set, TypeVar

T = TypeVar('T')

def common(collectionA: Iterable[T], collectionB: Iterable[T]) -> List[T]:
    collectionA_list = list(collectionA)
    collectionB_list = list(collectionB)
    accumulator: Set[T] = set()

    def processPair(indexX: int, indexY: int) -> None:
        nonlocal accumulator
        if indexX >= len(collectionA_list):
            return
        if indexY >= len(collectionB_list):
            processPair(indexX + 1, 0)
            return
        firstItem = collectionA_list[indexX]
        secondItem = collectionB_list[indexY]
        matched = secondItem == firstItem
        if matched:
            accumulator = accumulator.union({firstItem})
        processPair(indexX, indexY + 1)

    processPair(0, 0)
    return sorted(accumulator)