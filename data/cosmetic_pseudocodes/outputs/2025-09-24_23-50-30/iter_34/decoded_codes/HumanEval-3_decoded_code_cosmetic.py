from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    acc: int = 0
    for val in list_of_operations:
        acc += val
        if acc < 0:
            return True
    return False