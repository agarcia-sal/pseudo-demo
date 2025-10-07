from typing import List

def maximum(collection_of_ints: List[int], count_pos_int: int) -> List[int]:
    if count_pos_int == 0:
        return []
    sorted_list = sorted(collection_of_ints)
    length_val = len(sorted_list)
    start_idx = max(length_val - count_pos_int, 0)  # prevent negative index
    return sorted_list[start_idx:length_val]