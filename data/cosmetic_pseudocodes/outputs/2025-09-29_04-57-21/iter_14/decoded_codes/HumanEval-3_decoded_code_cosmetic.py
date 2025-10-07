from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    sum_accumulator: int = 0
    idx: int = 0
    while idx < len(list_of_operations):
        current_entry: int = list_of_operations[idx]
        sum_accumulator += current_entry
        if not (sum_accumulator >= 0):
            return True
        idx += 1
    return False