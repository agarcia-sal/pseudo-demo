from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    evens: List[T] = []
    odds: List[T] = []

    idx = 0
    while idx < len(list_of_elements):
        evens.append(list_of_elements[idx])
        idx += 2

    idx = 1
    while idx < len(list_of_elements):
        odds.append(list_of_elements[idx])
        idx += 2

    evens.sort()

    result: List[T] = []
    for i in range(min(len(evens), len(odds))):
        result.append(evens[i])
        result.append(odds[i])

    if len(evens) > len(odds):
        result.append(evens[-1])

    return result