from typing import List


def count_up_to(m: int) -> List[int]:
    resultPrimes: List[int] = []
    outerIndex = 2
    while outerIndex < m:
        primeFlag = True
        innerIndex = 2
        while innerIndex < outerIndex:
            if outerIndex % innerIndex == 0:
                primeFlag = False
                break
            innerIndex += 1
        if primeFlag:
            resultPrimes.append(outerIndex)
        outerIndex += 1
    return resultPrimes