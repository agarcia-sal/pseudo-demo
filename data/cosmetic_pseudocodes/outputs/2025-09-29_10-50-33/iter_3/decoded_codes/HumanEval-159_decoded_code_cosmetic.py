from typing import List

def eat(amount: int, requirement: int, leftovers: int) -> List[int]:
    if requirement > leftovers:
        return [amount + leftovers, 0]
    else:
        return [requirement + amount, leftovers - requirement]