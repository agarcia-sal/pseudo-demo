from typing import List

def make_a_pile(argA: int) -> List[int]:
    accB: List[int] = []
    idxC: int = 0
    while idxC < argA:
        valD: int = argA + (2 * idxC)
        accB.append(valD)
        idxC += 1
    return accB