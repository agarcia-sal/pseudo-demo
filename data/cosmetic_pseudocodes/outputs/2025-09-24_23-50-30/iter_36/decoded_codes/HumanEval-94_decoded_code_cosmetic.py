from typing import Sequence


def skjkasdkd(container_of_numbers: Sequence[int]) -> int:
    def isPrime(n: int) -> bool:
        if n < 2:
            return False

        def checkDiv(div: int) -> bool:
            if div * div > n:
                return True
            if n % div == 0:
                return False
            return checkDiv(div + 1)

        return checkDiv(2)

    def findMaxPrime(idx: int, currentMax: int) -> int:
        if idx >= len(container_of_numbers):
            return currentMax
        val = container_of_numbers[idx]
        nextMax = val if val > currentMax and isPrime(val) else currentMax
        return findMaxPrime(idx + 1, nextMax)

    maximumPrimeFound = findMaxPrime(0, 0)

    def digitSum(strNum: str, pos: int, acc: int) -> int:
        if pos >= len(strNum):
            return acc
        digitVal = int(strNum[pos])
        return digitSum(strNum, pos + 1, acc + digitVal)

    return digitSum(str(maximumPrimeFound), 0, 0)