from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    length = len(input_list)
    if length == 0:
        return []
    alpha = input_list[0]
    beta = input_list[-1]
    gamma: bool = ((alpha + beta) % 2) == 0
    return sorted(input_list, reverse=gamma)