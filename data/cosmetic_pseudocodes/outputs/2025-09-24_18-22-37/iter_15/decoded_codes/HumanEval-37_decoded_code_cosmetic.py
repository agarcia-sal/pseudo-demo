from typing import Sequence, List, TypeVar

T = TypeVar('T')


def sort_even(input_sequence: Sequence[T]) -> List[T]:
    primary_elements: List[T] = []
    secondary_elements: List[T] = []
    index_counter: int = 0

    while index_counter < len(input_sequence):
        if index_counter % 2 == 0:
            primary_elements.append(input_sequence[index_counter])
        else:
            secondary_elements.append(input_sequence[index_counter])
        index_counter += 1

    temp_var: int = len(primary_elements)
    temp_var2: int = len(secondary_elements)
    sort_index: int = 0

    # Bubble sort primary_elements in ascending order
    while sort_index < temp_var - 1:
        inner_index: int = 0
        while inner_index < temp_var - sort_index - 1:
            if primary_elements[inner_index] > primary_elements[inner_index + 1]:
                swap_temp: T = primary_elements[inner_index]
                primary_elements[inner_index] = primary_elements[inner_index + 1]
                primary_elements[inner_index + 1] = swap_temp
            inner_index += 1
        sort_index += 1

    assembled_list: List[T] = []
    zipper_index: int = 0

    while zipper_index < temp_var2:
        assembled_list.append(primary_elements[zipper_index])
        assembled_list.append(secondary_elements[zipper_index])
        zipper_index += 1

    if temp_var != temp_var2:
        assembled_list.append(primary_elements[temp_var - 1])

    return assembled_list