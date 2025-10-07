from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    evens: List[T] = []
    odds: List[T] = []
    cursor: int = 0
    while cursor < len(list_of_elements):
        evens.append(list_of_elements[cursor])
        cursor += 2
    pointer: int = 1
    while pointer < len(list_of_elements):
        odds.append(list_of_elements[pointer])
        pointer += 2
    evens.sort()
    merged_result: List[T] = []
    idx: int = 0
    while idx < len(odds):
        merged_result.append(evens[idx])
        merged_result.append(odds[idx])
        idx += 1
    if len(evens) > len(odds):
        merged_result.append(evens[-1])
    return merged_result