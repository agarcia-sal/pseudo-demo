from typing import Tuple

def eat(amount: int, requirement: int, stock: int) -> Tuple[int, int]:
    while True:
        if not (requirement > stock):
            return amount + requirement, stock - requirement
        else:
            return amount + stock, 0