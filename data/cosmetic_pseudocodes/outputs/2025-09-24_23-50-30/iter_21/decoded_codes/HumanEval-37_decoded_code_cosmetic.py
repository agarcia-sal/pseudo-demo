from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    def interleave(l1: List[T], l2: List[T], accumulator: List[T], idx: int) -> List[T]:
        if idx == len(l2):
            return accumulator + l1[idx:]
        return interleave(l1, l2, accumulator + [l1[idx], l2[idx]], idx + 1)

    evens: List[T] = []
    odds: List[T] = []
    for idx in range(len(list_of_elements)):
        if idx % 2 == 0:
            evens.append(list_of_elements[idx])
        else:
            odds.append(list_of_elements[idx])

    evens.sort()
    return interleave(evens, odds, [], 0)