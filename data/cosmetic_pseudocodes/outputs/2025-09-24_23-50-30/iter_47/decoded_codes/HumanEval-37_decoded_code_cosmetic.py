from typing import List, TypeVar

T = TypeVar('T')

def sort_in_non_decreasing_order(elements: List[T]) -> None:
    elements.sort()

def sort_even(list_of_elements: List[T]) -> List[T]:
    temp_list_1: List[T] = []
    temp_list_2: List[T] = []
    index_counter: int = 0

    while index_counter < len(list_of_elements):
        if index_counter % 2 == 0:
            temp_list_1.append(list_of_elements[index_counter])
        else:
            temp_list_2.append(list_of_elements[index_counter])
        index_counter += 1

    sort_in_non_decreasing_order(temp_list_1)

    result_list: List[T] = []
    ptr: int = 0

    while ptr < len(temp_list_2):
        result_list.append(temp_list_1[ptr])
        result_list.append(temp_list_2[ptr])
        ptr += 1

    if len(temp_list_1) > len(temp_list_2):
        result_list.append(temp_list_1[-1])

    return result_list