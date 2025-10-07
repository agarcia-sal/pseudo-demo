from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    tally: int = 0
    idx: int = 0
    while idx < len(list_of_operations):
        current_op: int = list_of_operations[idx]
        tally += current_op
        if tally < 0:
            return True
        idx += 1
    return False