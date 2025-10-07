from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    resultAccumulator: set[T] = set()

    iteratorA = iter(list1)
    while True:
        try:
            candidate = next(iteratorA)
        except StopIteration:
            break
        iteratorB = iter(list2)
        while True:
            try:
                comparisonValue = next(iteratorB)
            except StopIteration:
                break
            if candidate == comparisonValue:
                resultAccumulator.add(candidate)

    sortedOutput: List[T] = sorted(resultAccumulator)
    return sortedOutput