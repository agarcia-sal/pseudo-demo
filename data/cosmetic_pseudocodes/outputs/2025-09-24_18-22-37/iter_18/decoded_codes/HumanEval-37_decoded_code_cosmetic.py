from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    accumulator: List[T] = []
    first_subset: List[T] = []
    second_subset: List[T] = []
    x: int = 0
    while x < len(list_of_elements):
        first_subset.append(list_of_elements[x])
        x += 2
    y: int = 1
    while True:
        if y >= len(list_of_elements):
            break
        second_subset.append(list_of_elements[y])
        y += 2
    first_subset.sort()
    i: int = 0
    while True:
        if i >= len(second_subset):
            break
        accumulator.append(first_subset[i])
        accumulator.append(second_subset[i])
        i += 1
    if len(first_subset) > len(second_subset):
        accumulator.append(first_subset[-1])
    return accumulator