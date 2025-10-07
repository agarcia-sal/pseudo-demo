from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    temp_balance: int = 0
    index: int = 0
    while index < len(list_of_operations):
        temp_balance += list_of_operations[index]
        if temp_balance < 0:
            return True
        index += 1
    return False