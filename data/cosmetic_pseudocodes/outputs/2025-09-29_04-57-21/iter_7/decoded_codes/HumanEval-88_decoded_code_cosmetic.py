from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    if not input_list:
        return []
    boundary_sum = input_list[0] + input_list[-1]
    descending_flag = (boundary_sum % 2 == 0)
    return sorted(input_list, reverse=descending_flag)