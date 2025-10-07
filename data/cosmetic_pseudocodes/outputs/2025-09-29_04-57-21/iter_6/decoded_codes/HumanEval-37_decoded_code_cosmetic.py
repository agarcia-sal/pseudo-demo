from typing import List, TypeVar

T = TypeVar('T')


def sort_even(list_of_elements: List[T]) -> List[T]:
    first_partition: List[T] = []
    second_partition: List[T] = []
    idx: int = 0
    while idx < len(list_of_elements):
        first_partition.append(list_of_elements[idx])
        idx += 2

    idx = 1
    while idx < len(list_of_elements):
        second_partition.append(list_of_elements[idx])
        idx += 2

    first_partition.sort()

    merged_result: List[T] = []
    counter: int = 0
    while counter < len(second_partition) and counter < len(first_partition):
        merged_result.append(first_partition[counter])
        merged_result.append(second_partition[counter])
        counter += 1

    if len(first_partition) > len(second_partition):
        merged_result.append(first_partition[-1])

    return merged_result