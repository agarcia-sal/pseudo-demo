from typing import List


def count_up_to(n: int) -> List[int]:
    def verify_prime(candidate: int, divisor: int) -> bool:
        if divisor * divisor > candidate:
            return True
        elif candidate % divisor == 0:
            return False
        else:
            return verify_prime(candidate, divisor + 1)

    primesCollection: List[int] = []
    currentNumber = 2

    while currentNumber < n:
        if verify_prime(currentNumber, 2):
            primesCollection.append(currentNumber)
        currentNumber += 1

    return primesCollection