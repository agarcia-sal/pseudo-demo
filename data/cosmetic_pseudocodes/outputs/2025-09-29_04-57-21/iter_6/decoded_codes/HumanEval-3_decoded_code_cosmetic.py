from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    total = 0
    for idx in range(len(list_of_operations)):
        total += list_of_operations[idx]
        if total < 0:
            return True
    return False