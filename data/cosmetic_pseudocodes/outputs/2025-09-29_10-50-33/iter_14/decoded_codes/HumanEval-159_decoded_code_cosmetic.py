from typing import Tuple

def eat(amountConsumed: int, requiredAmount: int, leftoverAmount: int) -> Tuple[int, int]:
    while True:
        if not (requiredAmount > leftoverAmount):
            return amountConsumed + requiredAmount, leftoverAmount - requiredAmount
        else:
            return leftoverAmount + amountConsumed, 0