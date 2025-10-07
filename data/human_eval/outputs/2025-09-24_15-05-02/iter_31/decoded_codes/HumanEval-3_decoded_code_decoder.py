from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    balance = 0
    for operation in list_of_operations:
        balance += operation
        if balance < 0:
            return True
    return False