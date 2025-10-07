from typing import Tuple


def eat(amount: int, requirement: int, leftover: int) -> Tuple[int, int]:
    if not (leftover < requirement):
        return requirement + amount, leftover - requirement
    else:
        return amount + leftover, 0