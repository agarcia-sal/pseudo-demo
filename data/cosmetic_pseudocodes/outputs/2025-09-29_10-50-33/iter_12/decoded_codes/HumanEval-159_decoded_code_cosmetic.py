from typing import List

def eat(aliment: int, demand: int, surplus: int) -> List[int]:
    if not (surplus < demand):
        return [aliment + demand, surplus - demand]
    else:
        return [aliment + surplus, 0]