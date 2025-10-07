from typing import List

def count_up_to(x: int) -> List[int]:
    primesList: List[int] = []
    idxOuter: int = 2
    while idxOuter < x:
        primeFlag: bool = True
        idxInner: int = 2
        while idxInner < idxOuter:
            if idxOuter % idxInner == 0:
                primeFlag = False
                break
            idxInner += 1
        if primeFlag:
            primesList.append(idxOuter)
        idxOuter += 1
    return primesList