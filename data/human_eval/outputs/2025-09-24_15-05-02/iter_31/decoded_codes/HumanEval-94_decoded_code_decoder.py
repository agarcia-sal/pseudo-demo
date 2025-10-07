from math import isqrt
from typing import List

def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(number: int) -> bool:
        if number < 2:
            return False
        for divisor in range(2, isqrt(number) + 1):
            if number % divisor == 0:
                return False
        return True

    maximum_prime = 0
    index = 0
    while index < len(list_of_integers):
        n = list_of_integers[index]
        if n > maximum_prime and isPrime(n):
            maximum_prime = n
        index += 1

    return sum(int(d) for d in str(maximum_prime))