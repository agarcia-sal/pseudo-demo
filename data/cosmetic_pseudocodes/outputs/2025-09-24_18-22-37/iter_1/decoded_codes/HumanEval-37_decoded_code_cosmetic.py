from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    evens: List[T] = []
    odds: List[T] = []
    for i in range(len(list_of_elements)):
        if i % 2 == 0:
            evens.append(list_of_elements[i])
        else:
            odds.append(list_of_elements[i])
    evens.sort()
    result: List[T] = []
    min_len = min(len(evens), len(odds))
    for j in range(min_len):
        result.append(evens[j])
        result.append(odds[j])
    if len(evens) > len(odds):
        result.append(evens[-1])
    return result