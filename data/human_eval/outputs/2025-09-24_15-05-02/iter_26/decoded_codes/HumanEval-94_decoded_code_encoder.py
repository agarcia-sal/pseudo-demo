from math import isqrt
from typing import List

def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(number: int) -> bool:
        if number < 2:
            return False
        for i in range(2, isqrt(number) + 1):
            if number % i == 0:
                return False
        return True

    max_prime: int = 0
    index: int = 0
    while index < len(list_of_integers):
        current = list_of_integers[index]
        if current > max_prime and isPrime(current):
            max_prime = current
        index += 1

    result: int = sum(int(digit) for digit in str(max_prime))
    return result