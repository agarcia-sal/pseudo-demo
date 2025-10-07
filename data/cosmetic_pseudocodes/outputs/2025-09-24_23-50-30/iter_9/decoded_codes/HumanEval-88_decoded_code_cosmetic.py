from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    if not input_list:
        return []
    boundary_total: int = input_list[-1] + input_list[0]
    descending_flag: bool = (boundary_total % 2) == 0
    return sorted(input_list, reverse=descending_flag)