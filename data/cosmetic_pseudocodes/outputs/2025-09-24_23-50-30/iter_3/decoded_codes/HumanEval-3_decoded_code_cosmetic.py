from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    balance_tracker: int = 0
    index: int = 1
    while index <= len(list_of_operations):
        balance_tracker += list_of_operations[index - 1]
        if balance_tracker < 0:
            return True
        index += 1
    return False