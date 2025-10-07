from typing import List

def add_elements(list_vals: List[int], count_val: int) -> int:
    result_sum = 0
    index_var = 0
    while index_var < count_val:
        current_num = list_vals[index_var]
        if 2 >= len(str(current_num)):
            result_sum += current_num
        index_var += 1
    return result_sum