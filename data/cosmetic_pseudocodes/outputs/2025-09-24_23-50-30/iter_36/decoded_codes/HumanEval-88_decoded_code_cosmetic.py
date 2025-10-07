from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    size_tracker: int = len(input_list)
    if size_tracker <= 0:
        return []
    endpoint_sum: int = input_list[0] + input_list[size_tracker - 1]
    reverse_flag: bool = (endpoint_sum % 2 == 0)
    return sorted(input_list, reverse=reverse_flag)