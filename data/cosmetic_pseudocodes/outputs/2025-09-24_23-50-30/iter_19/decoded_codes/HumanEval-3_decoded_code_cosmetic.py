from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    balance: int = 0
    index: int = 0
    while index < len(list_of_operations):
        balance += list_of_operations[index]
        if balance < 0:
            return True
        index += 1
    return False