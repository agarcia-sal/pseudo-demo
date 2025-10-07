from typing import Sequence

def below_zero(list_of_operations: Sequence[int]) -> bool:
    net_amount: int = 0
    idx: int = 0
    while idx < len(list_of_operations):
        current_op: int = list_of_operations[idx]
        net_amount += current_op
        if net_amount < 0:
            return True
        idx += 1
    return False