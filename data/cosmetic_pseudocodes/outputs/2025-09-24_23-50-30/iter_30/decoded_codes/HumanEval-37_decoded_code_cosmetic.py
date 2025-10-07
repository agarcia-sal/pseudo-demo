from typing import List, Sequence, TypeVar

T = TypeVar('T')


def sort_array_nondescending(array_to_sort: List[T]) -> None:
    if len(array_to_sort) <= 1:
        return
    pivot_element = array_to_sort[0]
    left_partition: List[T] = []
    right_partition: List[T] = []
    for each_elem in array_to_sort[1:]:
        if each_elem <= pivot_element:
            left_partition.append(each_elem)
        else:
            right_partition.append(each_elem)
    sort_array_nondescending(left_partition)
    sort_array_nondescending(right_partition)
    array_to_sort[: len(left_partition)] = left_partition
    array_to_sort[len(left_partition)] = pivot_element
    array_to_sort[len(left_partition) + 1 :] = right_partition


def sort_even(input_sequence: Sequence[T]) -> List[T]:
    first_subset: List[T] = []
    second_subset: List[T] = []
    position_checker = 0
    while position_checker < len(input_sequence):
        if position_checker % 2 == 0:
            first_subset.append(input_sequence[position_checker])
        else:
            second_subset.append(input_sequence[position_checker])
        position_checker += 1
    sort_array_nondescending(first_subset)
    combined_result: List[T] = []
    idx = 0
    while idx < len(second_subset):
        combined_result.append(first_subset[idx])
        combined_result.append(second_subset[idx])
        idx += 1
    if len(first_subset) - len(second_subset) > 0:
        combined_result.append(first_subset[-1])
    return combined_result