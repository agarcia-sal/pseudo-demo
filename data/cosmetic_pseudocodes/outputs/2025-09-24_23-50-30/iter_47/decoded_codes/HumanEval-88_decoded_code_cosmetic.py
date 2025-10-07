from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    if len(input_list) == 0:
        return []
    temp_sum_var: int = input_list[0] + input_list[-1]
    is_desc_order_flag: bool = (temp_sum_var % 2 == 0)
    return sorted(input_list, reverse=is_desc_order_flag)