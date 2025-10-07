from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    total = 0
    index = 0
    while index < len(list_of_operations):
        total += list_of_operations[index]
        if total < 0:
            return True
        index += 1
    return False