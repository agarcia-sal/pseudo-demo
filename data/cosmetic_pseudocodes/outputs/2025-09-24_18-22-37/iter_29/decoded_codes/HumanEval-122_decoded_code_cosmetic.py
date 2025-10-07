from typing import List

def add_elements(input_list: List[int], count: int) -> int:
    total: int = 0
    idx: int = 0
    while idx < count:
        current_val: int = input_list[idx]
        str_val: str = str(current_val)
        len_str: int = len(str_val)
        if len_str <= 2:
            total += current_val
        idx += 1
    return total