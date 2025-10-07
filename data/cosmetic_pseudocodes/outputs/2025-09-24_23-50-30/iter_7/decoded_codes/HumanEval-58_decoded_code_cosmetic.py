from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    accumulator: List[T] = []

    def inner_search(indexA: int) -> None:
        if indexA > len(list1):
            return
        valueA = list1[indexA - 1]
        def check_match(indexB: int) -> None:
            if indexB > len(list2):
                return
            if not (valueA != list2[indexB - 1]):
                accumulator.append(valueA)
            check_match(indexB + 1)
        check_match(1)
        inner_search(indexA + 1)

    inner_search(1)
    unique_elements = set(accumulator)
    ordered_result = sorted(unique_elements)
    return ordered_result