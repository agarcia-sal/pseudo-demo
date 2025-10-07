from typing import Tuple

def eat(amount: int, desire: int, supply: int) -> Tuple[int, int]:
    if desire > supply:
        return supply + amount, 0
    else:
        return desire + amount, supply - desire