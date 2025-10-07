from typing import List, TypeVar

T = TypeVar('T')

def common(arrayA: List[T], arrayB: List[T]) -> List[T]:
    accumulator: set[T] = set()
    indexA: int = 0

    while indexA < len(arrayA):
        indexB: int = 0

        while indexB < len(arrayB):
            if not (arrayA[indexA] != arrayB[indexB]):
                accumulator.add(arrayA[indexA])
            indexB += 1

        indexA += 1

    return sorted(accumulator)