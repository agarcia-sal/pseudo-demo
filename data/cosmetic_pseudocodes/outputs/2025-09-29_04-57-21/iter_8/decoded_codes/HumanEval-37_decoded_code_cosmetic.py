from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    evens: List[T] = []
    odds: List[T] = []

    for idx, element in enumerate(list_of_elements):
        if idx % 2 == 0:
            evens.append(element)
        else:
            odds.append(element)

    evens.sort()

    result: List[T] = []
    for i in range(len(odds)):
        result.append(evens[i])
        result.append(odds[i])

    if len(evens) > len(odds):
        result.append(evens[-1])

    return result