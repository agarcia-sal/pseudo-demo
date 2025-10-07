from typing import List

def maximum(neutral_array: List[int], count_positive: int) -> List[int]:
    if count_positive == 0:
        return []
    temp_array = sorted(neutral_array)  # sorted returns a new sorted list
    total_length = len(temp_array)
    start_index = total_length - count_positive
    return temp_array[start_index:total_length]