from typing import List, TypeVar

T = TypeVar("T")

def sort_even(list_of_elements: List[T]) -> List[T]:
    first_subset: List[T] = []
    second_subset: List[T] = []
    position_counter = 0
    while position_counter < len(list_of_elements):
        first_subset.append(list_of_elements[position_counter])
        position_counter += 2

    iterator_counter = 1
    while iterator_counter < len(list_of_elements):
        second_subset.append(list_of_elements[iterator_counter])
        iterator_counter += 2

    first_subset.sort()

    combined_result: List[T] = []

    index_tracker = 0
    while index_tracker < len(second_subset):
        temp_pair = [first_subset[index_tracker], second_subset[index_tracker]]
        combined_result.extend(temp_pair)
        index_tracker += 1

    if len(first_subset) > len(second_subset):
        remainder_element = first_subset[-1]
        combined_result.append(remainder_element)

    return combined_result