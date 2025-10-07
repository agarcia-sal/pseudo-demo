from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    if input_list:
        temp_sum = input_list[0] + input_list[-1]
        order_descending_flag = (temp_sum - 2 * (temp_sum // 2)) == 0  # True if temp_sum is even
        return sorted(input_list, reverse=order_descending_flag)
    return []