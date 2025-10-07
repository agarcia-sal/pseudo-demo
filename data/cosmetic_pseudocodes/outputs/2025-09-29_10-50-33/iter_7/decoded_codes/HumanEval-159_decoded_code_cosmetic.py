from typing import List

def eat(quantity: int, demand: int, balance: int) -> List[int]:
    if demand <= balance:
        return [quantity + demand, balance - demand]
    else:
        return [quantity + balance, 0]