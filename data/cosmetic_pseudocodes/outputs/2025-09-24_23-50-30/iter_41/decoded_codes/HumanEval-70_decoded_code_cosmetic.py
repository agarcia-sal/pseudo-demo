from typing import List

def strange_sort_list(array_input: List[int]) -> List[int]:
    output_array: List[int] = []
    flip_flag: int = 1
    input_copy = array_input[:]  # Make a copy to avoid modifying original input
    while input_copy:
        if flip_flag == 1:
            chosen_value = min(input_copy)
        else:
            chosen_value = max(input_copy)
        output_array.append(chosen_value)
        input_copy.remove(chosen_value)
        flip_flag = 1 - flip_flag
    return output_array