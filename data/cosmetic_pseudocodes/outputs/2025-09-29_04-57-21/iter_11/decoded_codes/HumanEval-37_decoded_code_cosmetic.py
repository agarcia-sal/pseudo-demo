from typing import List, TypeVar

T = TypeVar('T')

def sort_even(array_of_items: List[T]) -> List[T]:
    evens: List[T] = []
    odds: List[T] = []
    counter = 0
    while counter < len(array_of_items):
        evens.append(array_of_items[counter])
        counter += 2
    counter = 1
    while counter < len(array_of_items):
        odds.append(array_of_items[counter])
        counter += 2
    evens.sort()
    merged_result: List[T] = []
    i = 0
    while i < len(odds):
        merged_result.append(evens[i])
        merged_result.append(odds[i])
        i += 1
    if len(evens) > len(odds):
        merged_result.append(evens[-1])
    return merged_result