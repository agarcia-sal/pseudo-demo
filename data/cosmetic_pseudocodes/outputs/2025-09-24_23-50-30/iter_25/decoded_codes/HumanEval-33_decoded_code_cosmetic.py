from typing import List

def sort_third(list_input: List[int]) -> List[int]:
    array_clone: List[int] = list_input[:]
    divisible_indices_values: List[int] = []

    index_counter: int = 0
    while index_counter < len(array_clone):
        if index_counter % 3 == 0:
            divisible_indices_values.append(array_clone[index_counter])
        index_counter += 1

    sorted_subset: List[int] = sorted(divisible_indices_values)

    index_counter = 0
    sorted_position: int = 0
    while index_counter < len(array_clone):
        if index_counter % 3 == 0:
            array_clone[index_counter] = sorted_subset[sorted_position]
            sorted_position += 1
        index_counter += 1

    return array_clone