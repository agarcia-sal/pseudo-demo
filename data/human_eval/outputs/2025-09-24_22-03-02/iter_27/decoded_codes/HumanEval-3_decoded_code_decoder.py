from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for index in range(len(operations)):
        op = operations[index]
        balance += op
        if balance < 0:
            return True
    return False