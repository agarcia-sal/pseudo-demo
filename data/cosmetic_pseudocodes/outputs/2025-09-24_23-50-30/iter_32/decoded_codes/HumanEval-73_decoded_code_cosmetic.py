from typing import List

def smallest_change(input_list: List[int]) -> int:
    total_mismatch = 0
    length = len(input_list)
    for i in range(length // 2):
        if input_list[i] != input_list[length - i - 1]:
            total_mismatch += 1
    return total_mismatch