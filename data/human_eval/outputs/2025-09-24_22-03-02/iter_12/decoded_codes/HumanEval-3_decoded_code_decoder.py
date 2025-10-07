from typing import List

def below_zero(OPERATIONS: List[int]) -> bool:
    balance = 0
    for op in OPERATIONS:
        balance += op
        if balance < 0:
            return True
    return False