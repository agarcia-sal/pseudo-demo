from typing import List

def eat(number: int, need: int, remaining: int) -> List[int]:
    if remaining >= need:
        newNumber = number + need
        newRemaining = remaining - need
        return [newNumber, newRemaining]
    else:
        return [number + remaining, 0]