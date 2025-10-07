from typing import List

def maximum(input_list: List[int], size_limit: int) -> List[int]:
    if size_limit == 0:
        return []
    sorted_list = sorted(input_list)
    total_len = len(input_list)
    start_index = total_len - size_limit
    return sorted_list[start_index:total_len]