from typing import List, Sequence, TypeVar

T = TypeVar('T')

def sort_even(sequence: Sequence[T]) -> List[T]:
    first_subset: List[T] = []
    second_subset: List[T] = []
    iterator_index: int = 0
    while iterator_index < len(sequence):
        if iterator_index % 2 == 0:
            first_subset.append(sequence[iterator_index])
        else:
            second_subset.append(sequence[iterator_index])
        iterator_index += 1

    sorted_first_subset: List[T] = sorted(first_subset)

    result_container: List[T] = []
    merge_index: int = 0
    while merge_index < len(second_subset):
        result_container.append(sorted_first_subset[merge_index])
        result_container.append(second_subset[merge_index])
        merge_index += 1

    if len(sorted_first_subset) > len(second_subset):
        result_container.append(sorted_first_subset[-1])

    return result_container