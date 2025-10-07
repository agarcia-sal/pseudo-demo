from typing import List

def add_elements(arr_vals: List[int], k: int) -> int:
    total_sum: int = 0
    counter: int = 0
    while counter < k:
        current_val: int = arr_vals[counter]
        if len(str(current_val)) <= 2:
            total_sum += current_val
        counter += 1
    return total_sum