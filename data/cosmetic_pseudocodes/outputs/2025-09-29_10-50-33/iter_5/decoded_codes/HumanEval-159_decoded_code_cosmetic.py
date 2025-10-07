from typing import List

def eat(currentValue: int, requiredAmount: int, availableAmount: int) -> List[int]:
    if availableAmount < requiredAmount:
        return [currentValue + availableAmount, 0]
    else:
        return [requiredAmount + currentValue, availableAmount - requiredAmount]