from typing import List

def eat(amount: int, want: int, balance: int) -> List[int]:
    if not (want > balance):
        return [want + amount, balance - want]
    return [balance + amount, 0]