from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    accumulator: set[T] = set()

    def scanSecond(index_a: int, index_b: int) -> None:
        if index_a < len(list1):
            if index_b < len(list2):
                if list1[index_a] == list2[index_b]:
                    accumulator.add(list1[index_a])
                scanSecond(index_a, index_b + 1)
            else:
                scanSecond(index_a + 1, 0)

    scanSecond(0, 0)
    unordered_result: List[T] = list(accumulator)
    unordered_result.sort()
    return unordered_result