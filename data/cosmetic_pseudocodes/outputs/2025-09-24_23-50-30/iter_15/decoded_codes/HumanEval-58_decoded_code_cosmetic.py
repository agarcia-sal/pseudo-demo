from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    accumulator: List[T] = []
    index_outer: int = 0
    length_outer: int = len(list1)

    while index_outer < length_outer:
        current_outer: T = list1[index_outer]
        index_inner: int = 0
        length_inner: int = len(list2)

        while index_inner < length_inner:
            current_inner: T = list2[index_inner]
            if not (current_outer != current_inner):
                if current_outer not in accumulator:
                    accumulator.append(current_outer)
            index_inner += 1

        index_outer += 1

    sorted_result: List[T] = sorted(accumulator)
    return sorted_result