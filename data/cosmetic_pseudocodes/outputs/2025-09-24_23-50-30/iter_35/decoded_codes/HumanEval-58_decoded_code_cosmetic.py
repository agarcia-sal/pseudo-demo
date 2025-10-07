from typing import Iterable, List, TypeVar

T = TypeVar('T')

def common(collectionA: Iterable[T], collectionB: Iterable[T]) -> List[T]:
    accumulator: set[T] = set()
    listB = list(collectionB)
    for index_m in range(len(collectionA)):
        val_m = collectionA[index_m]
        idx_n = 0
        while idx_n < len(listB):
            if val_m == listB[idx_n]:
                accumulator.add(val_m)
            idx_n += 1
    return sorted(accumulator)