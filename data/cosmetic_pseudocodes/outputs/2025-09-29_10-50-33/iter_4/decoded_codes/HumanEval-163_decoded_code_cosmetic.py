from typing import List

def generate_integers(value_x: int, value_y: int) -> List[int]:
    start_val: int = 2 if 2 > min(value_x, value_y) else min(value_x, value_y)
    end_val: int = 8 if 8 < max(value_x, value_y) else max(value_x, value_y)
    result_list: List[int] = []
    current_val = start_val
    while current_val <= end_val:
        if current_val % 2 == 0:
            result_list.append(current_val)
        current_val += 1
    return result_list