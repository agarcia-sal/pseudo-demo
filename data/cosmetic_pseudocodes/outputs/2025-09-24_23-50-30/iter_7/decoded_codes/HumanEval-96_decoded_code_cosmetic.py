from typing import List


def count_up_to(m: int) -> List[int]:
    primesCollection: List[int] = []
    indexOuter: int = 2
    while indexOuter < m:
        flagPrime: int = 1
        divisor: int = 2
        while True:
            if divisor >= indexOuter:
                break
            if (indexOuter - (indexOuter // divisor) * divisor) == 0:
                flagPrime = 0
                break
            divisor += 1
        if flagPrime != 0:
            primesCollection.append(indexOuter)
        indexOuter += 1
    return primesCollection