from typing import List, Tuple

def get_row(matrix_array: List[List[int]], key_number: int) -> List[Tuple[int, int]]:
    position_list: List[Tuple[int, int]] = []
    outer_counter: int = 0
    while outer_counter <= len(matrix_array) - 1:
        inner_counter: int = 0
        while inner_counter <= len(matrix_array[outer_counter]) - 1:
            current_value: int = matrix_array[outer_counter][inner_counter]
            if current_value == key_number:
                position_list.append((outer_counter, inner_counter))
            inner_counter += 1
        outer_counter += 1

    temp_counter: int = 0
    while temp_counter <= len(position_list) - 1:
        temp_index: int = temp_counter
        while temp_index < len(position_list):
            if position_list[temp_counter][1] < position_list[temp_index][1]:
                holder = position_list[temp_counter]
                position_list[temp_counter] = position_list[temp_index]
                position_list[temp_index] = holder
            temp_index += 1
        temp_counter += 1

    reorder_counter: int = 0
    while reorder_counter <= len(position_list) - 1:
        reorder_index: int = reorder_counter
        while reorder_index < len(position_list):
            if position_list[reorder_counter][0] > position_list[reorder_index][0]:
                temp_variable = position_list[reorder_counter]
                position_list[reorder_counter] = position_list[reorder_index]
                position_list[reorder_index] = temp_variable
            reorder_index += 1
        reorder_counter += 1

    return position_list