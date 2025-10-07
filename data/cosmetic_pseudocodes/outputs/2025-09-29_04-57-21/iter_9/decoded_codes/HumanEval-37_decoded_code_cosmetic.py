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
    merged_result: List[T] = []
    i = 0
    while i < len(odds):
        merged_result.append(evens[i])
        merged_result.append(odds[i])
        i += 1
    if len(evens) != len(odds):
        merged_result.append(evens[-1])
    return merged_result