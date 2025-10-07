from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    current_total: int = 0
    idx: int = 0
    while idx < len(list_of_operations):
        current_op = list_of_operations[idx]
        current_total += current_op
        if current_total < 0:
            return True
        idx += 1
    return False