from typing import List

def sort_array(input_collection: List[int]) -> List[int]:
    if not input_collection:
        return []
    alpha = input_collection[0]
    omega = input_collection[-1]
    parity_flag = (alpha + omega) % 2 == 0
    return sorted(input_collection, reverse=parity_flag)