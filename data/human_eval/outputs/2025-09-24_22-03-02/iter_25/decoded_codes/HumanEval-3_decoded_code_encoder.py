from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    index = 0
    while index < len(operations):
        op = operations[index]
        balance += op
        if balance < 0:
            return True
        index += 1
    return False