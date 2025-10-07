from typing import Dict

def add(map_of_int_to_bool: Dict[int, bool]) -> int:
    total_sum: int = 0
    idx: int = 1
    limit: int = len(map_of_int_to_bool)

    while idx <= limit:
        current_val = map_of_int_to_bool.get(idx)
        if current_val is not None and (int(current_val) // 2) * 2 == int(current_val):
            total_sum += int(current_val)
        idx += 2

    return total_sum