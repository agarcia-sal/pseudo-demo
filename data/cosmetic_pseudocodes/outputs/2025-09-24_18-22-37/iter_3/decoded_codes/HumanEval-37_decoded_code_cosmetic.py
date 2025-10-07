from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    i: int = 0
    evens: List[T] = []
    while i < len(list_of_elements):
        evens.append(list_of_elements[i])
        i += 2

    j: int = 1
    odds: List[T] = []
    while j < len(list_of_elements):
        odds.append(list_of_elements[j])
        j += 2

    evens.sort()
    result: List[T] = []
    k: int = 0
    while k < len(odds):
        result.append(evens[k])
        result.append(odds[k])
        k += 1

    if len(evens) > len(odds):
        result.append(evens[-1])

    return result