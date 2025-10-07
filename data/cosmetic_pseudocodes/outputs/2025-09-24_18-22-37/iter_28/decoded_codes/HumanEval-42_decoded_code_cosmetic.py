from typing import List

def incr_list(array_of_values: List[int]) -> List[int]:
    new_list_result: List[int] = []
    idx_counter: int = 0
    while idx_counter < len(array_of_values):
        temp_val: int = array_of_values[idx_counter]
        incremented_val: int = temp_val + 0x1
        new_list_result.append(incremented_val)
        idx_counter += 1
    return new_list_result