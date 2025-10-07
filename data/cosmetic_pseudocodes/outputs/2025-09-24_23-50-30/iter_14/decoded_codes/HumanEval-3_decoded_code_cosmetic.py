from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    accumulator: int = 0
    index: int = 0
    while index < len(list_of_operations):
        accumulator += list_of_operations[index]
        if accumulator < 0:
            return True
        index += 1
    return False