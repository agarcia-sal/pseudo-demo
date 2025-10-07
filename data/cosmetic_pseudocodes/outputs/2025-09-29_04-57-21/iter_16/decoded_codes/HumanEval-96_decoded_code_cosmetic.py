from typing import List

def count_up_to(n: int) -> List[int]:
    primesList: List[int] = []
    currentVal: int = 2

    while currentVal < n:
        primeFlag: int = 1
        divisor: int = 2

        while divisor < currentVal and primeFlag == 1:
            if currentVal % divisor == 0:
                primeFlag = 0
            else:
                divisor += 1

        if primeFlag == 1:
            primesList.append(currentVal)

        currentVal += 1

    return primesList