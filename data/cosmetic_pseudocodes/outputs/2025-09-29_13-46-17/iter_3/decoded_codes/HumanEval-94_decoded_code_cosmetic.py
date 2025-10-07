from typing import List


def skjkasdkd(inputArray: List[int]) -> int:
    def isPrime(num: int) -> bool:
        def checkDivisor(div: int) -> bool:
            if div * div > num:
                return True
            if num % div != 0:
                return checkDivisor(div + 1)
            else:
                return False

        if num < 2:
            return False
        return checkDivisor(2)

    highestPrime: int = 0
    pointer: int = 0

    while pointer < len(inputArray):
        currentVal = inputArray[pointer]
        if currentVal > highestPrime and isPrime(currentVal):
            highestPrime = currentVal
        pointer += 1

    totalDigitSum: int = 0
    digitsString = str(highestPrime)

    for charDigit in digitsString:
        totalDigitSum += int(charDigit)

    return totalDigitSum