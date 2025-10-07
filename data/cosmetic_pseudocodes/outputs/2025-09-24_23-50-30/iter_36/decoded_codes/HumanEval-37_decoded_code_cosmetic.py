from typing import List, TypeVar

T = TypeVar("T")

def sort_even(list_of_elements: List[T]) -> List[T]:
    accumulator: List[T] = []
    left_partition: List[T] = []
    right_partition: List[T] = []

    for index in range(len(list_of_elements)):
        if index % 2 == 0:
            left_partition.append(list_of_elements[index])
        else:
            right_partition.append(list_of_elements[index])

    left_partition.sort()
    iterator_left = 0
    iterator_right = 0

    while iterator_left < len(left_partition) and iterator_right < len(right_partition):
        accumulator.append(left_partition[iterator_left])
        accumulator.append(right_partition[iterator_right])
        iterator_left += 1
        iterator_right += 1

    if len(left_partition) > len(right_partition):
        accumulator.append(left_partition[iterator_left])

    return accumulator