from typing import List

def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        if integer_value < 2:
            return False
        divisor_candidate = 2
        while True:
            if divisor_candidate * divisor_candidate > integer_value:
                break
            if (integer_value % divisor_candidate) == 0:
                return False
            divisor_candidate += 1
        return True

    maxPrime: int = 0
    for position in range(len(list_of_integers)):
        currentNumber = list_of_integers[position]
        if currentNumber > maxPrime:
            if isPrime(currentNumber):
                maxPrime = currentNumber

    digitTotal: int = 0
    charIndex: int = 1
    maxPrimeStr = str(maxPrime)
    while charIndex <= len(maxPrimeStr):
        # charIndex is 1-based; convert to 0-based for indexing
        digitTotal += int(maxPrimeStr[charIndex - 1])
        charIndex += 1

    return digitTotal