from typing import List

def count_up_to(p: int) -> List[int]:
    primesList: List[int] = []
    iCounter: int = 2
    while iCounter < p:
        primeFlag: bool = True
        jCounter: int = 2
        while jCounter < iCounter:
            if iCounter % jCounter == 0:
                primeFlag = False
                break
            jCounter += 1
        if primeFlag:
            primesList.append(iCounter)
        iCounter += 1
    return primesList