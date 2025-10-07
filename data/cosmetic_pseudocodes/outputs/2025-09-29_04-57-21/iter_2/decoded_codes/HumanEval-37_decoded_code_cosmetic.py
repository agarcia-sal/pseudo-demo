from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    first_subset: List[T] = []
    second_subset: List[T] = []
    total_length: int = len(list_of_elements)
    i: int = 0
    while i < total_length:
        if i % 2 == 0:
            first_subset.append(list_of_elements[i])
        else:
            second_subset.append(list_of_elements[i])
        i += 1

    first_subset.sort()

    combined_result: List[T] = []
    idx: int = 0
    while idx < len(second_subset):
        combined_result.append(first_subset[idx])
        combined_result.append(second_subset[idx])
        idx += 1

    if len(first_subset) != len(second_subset):
        combined_result.append(first_subset[-1])

    return combined_result