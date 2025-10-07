from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    current_sum: int = 0
    iterator: int = 0
    while iterator < len(list_of_operations):
        current_sum += list_of_operations[iterator]
        if current_sum < 0:
            return True
        iterator += 1
    return False