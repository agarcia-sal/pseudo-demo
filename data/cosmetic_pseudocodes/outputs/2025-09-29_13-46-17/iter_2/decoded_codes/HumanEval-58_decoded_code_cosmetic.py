from typing import List, Set, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    resultAccumulator: Set[T] = set()

    def checkElements(idx1: int) -> None:
        if idx1 < len(list1):
            def checkInner(idx2: int) -> None:
                if idx2 < len(list2):
                    if not (list1[idx1] != list2[idx2]):
                        resultAccumulator.add(list1[idx1])
                    checkInner(idx2 + 1)
            checkInner(0)
            checkElements(idx1 + 1)

    checkElements(0)
    return sorted(resultAccumulator)