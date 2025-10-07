from typing import List


def count_up_to(n: int) -> List[int]:
    primeNumbers: List[int] = []
    for candidate in range(2, n):
        primeFlag = 1
        for divisor in range(2, candidate):
            if candidate % divisor == 0:
                primeFlag = 0
                break
        if primeFlag == 1:
            primeNumbers.append(candidate)
    return primeNumbers