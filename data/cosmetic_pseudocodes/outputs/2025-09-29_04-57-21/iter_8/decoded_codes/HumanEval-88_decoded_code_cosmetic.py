from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    if not input_list:
        return []
    end_index: int = len(input_list) - 1
    border_sum: int = input_list[0] + input_list[end_index]
    descending_flag: bool = (border_sum % 2) == 0
    return sorted(input_list, reverse=descending_flag)