from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    if not len(input_list) > 0:
        return []
    boundary_sum = input_list[-1] + input_list[0]
    desc_flag = (boundary_sum % 2 == 0)
    return sorted(input_list, reverse=desc_flag)