from typing import Sequence, List, Set, TypeVar

T = TypeVar('T', bound=int)  # assuming elements support subtraction and ordering as ints

def common(collectionA: Sequence[T], collectionB: Sequence[T]) -> List[T]:
    def recurse(indexA: int, accumulator: Set[T]) -> Set[T]:
        if indexA >= len(collectionA):
            return accumulator

        def innerLoop(indexB: int, currentAccumulator: Set[T]) -> Set[T]:
            if indexB >= len(collectionB):
                return currentAccumulator
            if collectionA[indexA] == collectionB[indexB]:
                return innerLoop(indexB + 1, currentAccumulator | {collectionA[indexA]})
            else:
                return innerLoop(indexB + 1, currentAccumulator)

        return recurse(indexA + 1, innerLoop(0, accumulator))

    accumulated_set = recurse(0, set())
    sorted_list = list(accumulated_set)
    sorted_list.sort(key=lambda x: x)  # natural ascending order; comparison is a - b implicitly
    return sorted_list