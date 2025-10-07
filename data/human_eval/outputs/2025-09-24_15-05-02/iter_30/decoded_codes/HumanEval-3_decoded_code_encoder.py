from typing import Iterable

def below_zero(operations: Iterable[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False