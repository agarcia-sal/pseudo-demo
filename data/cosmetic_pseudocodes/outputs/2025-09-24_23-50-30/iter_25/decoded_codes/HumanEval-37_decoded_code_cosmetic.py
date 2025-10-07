from typing import List, TypeVar

T = TypeVar('T')

def sort_non_decreasing(arr: List[T]) -> None:
    arr.sort()

def sort_even(list_of_elements: List[T]) -> List[T]:
    first_partition: List[T] = []
    second_partition: List[T] = []
    idx = 0
    n = len(list_of_elements)
    while idx < n:
        first_partition.append(list_of_elements[idx])
        if idx + 1 < n:
            second_partition.append(list_of_elements[idx + 1])
        idx += 2

    sort_non_decreasing(first_partition)

    merged_result: List[T] = []
    pos = 0
    while pos < len(second_partition):
        merged_result.append(first_partition[pos])
        merged_result.append(second_partition[pos])
        pos += 1

    if len(first_partition) >= len(second_partition):
        merged_result.append(first_partition[-1])

    return merged_result