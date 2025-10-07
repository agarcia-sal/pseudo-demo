from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    accumulator: List[T] = []
    first_subset: List[T] = []
    second_subset: List[T] = []

    for idx, element in enumerate(list_of_elements):
        if idx % 2 == 0:
            first_subset.append(element)
        else:
            second_subset.append(element)

    first_subset.sort()
    len_first = len(first_subset)
    len_second = len(second_subset)

    for i in range(len_second):
        accumulator.append(first_subset[i])
        accumulator.append(second_subset[i])

    if len_first > len_second:
        accumulator.append(first_subset[-1])

    return accumulator