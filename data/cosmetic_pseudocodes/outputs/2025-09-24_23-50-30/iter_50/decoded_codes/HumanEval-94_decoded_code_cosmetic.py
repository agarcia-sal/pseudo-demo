from math import sqrt
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        def checkDivisor(current_divisor: int, limit: int) -> bool:
            if current_divisor >= limit:
                return True
            if integer_value % current_divisor == 0:
                return False
            return checkDivisor(current_divisor + 1, limit)

        if integer_value < 2:
            return False
        limit = int(sqrt(integer_value)) + 1
        return checkDivisor(2, limit)

    highestPrimeSoFar = 0
    positionCursor = 0
    while positionCursor < len(list_of_integers):
        candidateValue = list_of_integers[positionCursor]
        if candidateValue > highestPrimeSoFar and isPrime(candidateValue):
            highestPrimeSoFar = candidateValue
        positionCursor += 1

    digitSum = 0
    stringRepresentation = str(highestPrimeSoFar)
    for singleChar in stringRepresentation:
        digitSum += ord(singleChar) - ord('0')

    return digitSum