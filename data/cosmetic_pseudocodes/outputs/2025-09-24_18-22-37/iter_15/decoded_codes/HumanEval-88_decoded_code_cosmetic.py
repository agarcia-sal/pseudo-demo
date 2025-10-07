from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    if len(input_list) == 0:
        return []
    tmp1: int = input_list[0]
    tmp2: int = len(input_list) - 1
    initial_value: int = tmp1 + input_list[tmp2]

    order_flag: bool = (initial_value % 2 == 0)

    return sorted(input_list, reverse=order_flag)