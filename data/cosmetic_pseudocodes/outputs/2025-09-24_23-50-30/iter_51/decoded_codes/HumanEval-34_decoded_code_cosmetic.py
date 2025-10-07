from typing import List, TypeVar, Set

T = TypeVar('T')

def unique(arr: List[T]) -> List[T]:
    def buildSet(seq: List[T], idx: int, accumSet: Set[T]) -> Set[T]:
        if idx == len(seq):
            return accumSet
        else:
            accumSet.add(seq[idx])
            return buildSet(seq, idx + 1, accumSet)
    distinctSet = buildSet(arr, 0, set())
    sortedList = sorted(distinctSet)
    return sortedList