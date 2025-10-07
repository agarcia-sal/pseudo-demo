from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    balance: int = 0
    for op in list_of_operations:
        balance += op
        if balance < 0:
            return True
    return False