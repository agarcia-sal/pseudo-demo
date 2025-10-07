from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    delta: int = 0
    index: int = 0
    while index < len(list_of_operations):
        delta += list_of_operations[index]
        if delta < 0:
            return True
        index += 1
    return False