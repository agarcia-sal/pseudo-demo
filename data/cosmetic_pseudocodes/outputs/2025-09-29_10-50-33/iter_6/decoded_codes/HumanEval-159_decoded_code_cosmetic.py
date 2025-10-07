from typing import Tuple

def eat(amount: int, required: int, balance: int) -> Tuple[int, int]:
    if required <= balance:
        return amount + required, balance - required
    else:
        return amount + balance, 0