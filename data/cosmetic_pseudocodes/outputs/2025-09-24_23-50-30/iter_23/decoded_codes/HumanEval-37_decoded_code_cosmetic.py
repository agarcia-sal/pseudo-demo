from typing import Sequence, TypeVar, List

T = TypeVar('T')

def sort_even(list_of_elements: Sequence[T]) -> List[T]:
    first_subset: List[T] = [list_of_elements[i] for i in range(0, len(list_of_elements), 2)]
    second_subset: List[T] = [list_of_elements[i] for i in range(1, len(list_of_elements), 2)]
    first_subset.sort()
    result_sequence: List[T] = []
    min_len = min(len(first_subset), len(second_subset))
    for i in range(min_len):
        result_sequence.append(first_subset[i])
        result_sequence.append(second_subset[i])
    if len(first_subset) > len(second_subset):
        result_sequence.append(first_subset[-1])
    return result_sequence