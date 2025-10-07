from typing import Iterable

def below_zero(operations: Iterable[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False