from typing import List

def sort_third(list_input_param: List[int]) -> List[int]:
    temp_list: List[int] = list(list_input_param)
    values_div_by_three: List[int] = []
    idx_counter: int = 0
    while idx_counter < len(temp_list):
        if idx_counter % 3 == 0:
            values_div_by_three.append(temp_list[idx_counter])
        idx_counter += 1

    sorted_values_divisible_to_three: List[int] = sorted(values_div_by_three)

    write_index: int = 0
    idx_counter = 0
    while idx_counter < len(temp_list):
        if idx_counter % 3 == 0:
            temp_list[idx_counter] = sorted_values_divisible_to_three[write_index]
            write_index += 1
        idx_counter += 1

    return temp_list