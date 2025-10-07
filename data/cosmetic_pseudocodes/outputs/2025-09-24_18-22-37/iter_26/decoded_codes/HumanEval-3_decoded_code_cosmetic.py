from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    acc: int = 0
    idx: int = 0
    while idx < len(list_of_operations):
        current_op: int = list_of_operations[idx]
        temp_sum: int = acc + current_op
        acc = temp_sum
        if acc < 0:
            return True
        idx += 1
    return False