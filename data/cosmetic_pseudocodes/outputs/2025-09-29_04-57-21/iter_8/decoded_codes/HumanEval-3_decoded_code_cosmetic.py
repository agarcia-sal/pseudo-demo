from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    total_balance: int = 0
    iterator: int = 0

    while iterator < len(list_of_operations):
        current_value: int = list_of_operations[iterator]
        total_balance = current_value + total_balance

        if not (total_balance >= 0):
            return True
        iterator += 1

    return False