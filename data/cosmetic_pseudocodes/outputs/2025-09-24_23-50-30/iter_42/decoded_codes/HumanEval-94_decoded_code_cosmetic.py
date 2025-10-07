from typing import List


def skjkasdkd(array_numbers: List[int]) -> int:
    def isPrime(value_int: int) -> bool:
        if value_int < 2:
            return False
        checkDivisor = 2
        limit = int(value_int**0.5 + 0.9999999999)
        while checkDivisor <= limit:
            if value_int % checkDivisor == 0:
                return False
            checkDivisor += 1
        return True

    currentMaxPrime = 0
    walker = 0
    length = len(array_numbers)
    while walker < length:
        if array_numbers[walker] > currentMaxPrime and isPrime(array_numbers[walker]):
            currentMaxPrime = array_numbers[walker]
        walker += 1

    digitSum = 0
    digitsList = list(str(currentMaxPrime))
    for digitChar in digitsList:
        digitSum += int(digitChar)

    return digitSum