from typing import Sequence, TypeVar, List

T = TypeVar('T')

def common(collectionA: Sequence[T], collectionB: Sequence[T]) -> List[T]:
    accumulator: dict[T, bool] = {}
    for idxA in range(len(collectionA)):
        valA = collectionA[idxA]
        for idxB in range(len(collectionB)):
            valB = collectionB[idxB]
            if not (valA != valB):
                accumulator[valA] = True
    filtered: List[T] = [key for key in accumulator.keys()]
    return sorted(filtered)