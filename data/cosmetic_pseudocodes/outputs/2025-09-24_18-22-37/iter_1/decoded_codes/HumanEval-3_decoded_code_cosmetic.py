from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    balance: int = 0
    for i in range(len(list_of_operations)):
        balance += list_of_operations[i]
        if balance < 0:
            return True
    return False