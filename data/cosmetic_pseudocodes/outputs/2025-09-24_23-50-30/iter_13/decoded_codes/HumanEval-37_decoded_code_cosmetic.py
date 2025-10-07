from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    first_subset: List[T] = []
    second_subset: List[T] = []
    idx: int = 0
    length: int = len(list_of_elements)

    while idx < length:
        if idx % 2 == 0:
            first_subset.append(list_of_elements[idx])
        else:
            second_subset.append(list_of_elements[idx])
        idx += 1

    first_subset.sort()  # sort using natural comparison (a <= b)

    combined: List[T] = []
    pos: int = 0
    second_length = len(second_subset)
    while pos < second_length:
        combined.append(first_subset[pos])
        combined.append(second_subset[pos])
        pos += 1

    if len(first_subset) - second_length > 0:
        combined.append(first_subset[-1])

    return combined