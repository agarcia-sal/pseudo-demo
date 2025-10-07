from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    total: int = 0
    index: int = 0

    while index < len(list_of_operations):
        total += list_of_operations[index]
        if not (total >= 0):
            return True
        index += 1

    return False