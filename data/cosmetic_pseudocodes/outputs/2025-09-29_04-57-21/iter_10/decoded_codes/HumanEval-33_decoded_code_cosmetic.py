from typing import List

def sort_third(list_input: List[int]) -> List[int]:
    duplicate_list: List[int] = list_input[:]
    selected_values: List[int] = []
    current_index: int = 0

    while current_index < len(duplicate_list):
        if current_index % 3 == 0:
            selected_values.append(duplicate_list[current_index])
        current_index += 1

    sorted_selected_values: List[int] = sorted(selected_values)

    replacement_index: int = 0
    position_pointer: int = 0

    while position_pointer < len(duplicate_list):
        if position_pointer % 3 == 0:
            duplicate_list[position_pointer] = sorted_selected_values[replacement_index]
            replacement_index += 1
        position_pointer += 1

    return duplicate_list