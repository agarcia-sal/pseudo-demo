from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    idx: int = 0
    acc: int = 0
    while idx < len(list_of_operations):
        acc += list_of_operations[idx]
        if acc < 0:
            return True
        idx += 1
    return False