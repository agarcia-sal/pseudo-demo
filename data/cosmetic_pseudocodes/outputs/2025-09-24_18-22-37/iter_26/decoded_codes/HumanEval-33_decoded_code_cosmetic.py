from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    temporary_list: List[T] = list_input.copy()
    selected_elements: List[T] = []
    temp_index: int = 0

    while temp_index < len(temporary_list):
        if temp_index % 3 == 0:
            selected_elements.append(temporary_list[temp_index])
        temp_index += 1

    ordered_elements: List[T] = sorted(selected_elements)

    replace_index: int = 0
    total_length: int = len(temporary_list)

    for curr_pos in range(total_length):
        if curr_pos % 3 == 0:
            temporary_list[curr_pos] = ordered_elements[replace_index]
            replace_index += 1

    return temporary_list