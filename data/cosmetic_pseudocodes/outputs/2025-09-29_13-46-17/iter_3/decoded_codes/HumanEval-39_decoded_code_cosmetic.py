from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        def checkDivisor(currentDivisor: int, maxDivisor: int) -> bool:
            if currentDivisor > maxDivisor:
                return True
            if integer_p % currentDivisor == 0:
                return False
            return checkDivisor(currentDivisor + 1, maxDivisor)

        sqrtLimit = isqrt(integer_p) + 1
        maxCheck = sqrtLimit
        if integer_p - 1 < sqrtLimit:
            maxCheck = integer_p - 1

        return checkDivisor(2, maxCheck)

    fibonacciSequence: List[int] = [0, 1]

    def primeFibHelper(primesRemaining: int) -> int:
        lastIndex = len(fibonacciSequence) - 1
        nextVal = fibonacciSequence[lastIndex] + fibonacciSequence[lastIndex - 1]
        fibonacciSequence.append(nextVal)

        if is_prime(nextVal):
            primesRemaining -= 1
            if primesRemaining == 0:
                return nextVal

        return primeFibHelper(primesRemaining)

    return primeFibHelper(integer_n)