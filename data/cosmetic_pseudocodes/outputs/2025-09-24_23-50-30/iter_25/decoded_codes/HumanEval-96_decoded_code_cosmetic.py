from typing import List


def count_up_to(m: int) -> List[int]:
    accumulatedPrimes: List[int] = []

    def checkDivisor(candidate: int, divisor: int) -> bool:
        if divisor >= candidate:
            return True
        elif candidate % divisor == 0:
            return False
        else:
            return checkDivisor(candidate, divisor + 1)

    for iterator in range(2, m):
        if checkDivisor(iterator, 2):
            accumulatedPrimes.append(iterator)

    return accumulatedPrimes