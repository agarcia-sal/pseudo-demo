from math import sqrt, floor
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(n: int) -> bool:
        if n < 2:
            return False
        limit = floor(sqrt(n))
        for divisor in range(2, limit + 1):
            if n % divisor == 0:
                return False
        return True

    highest_prime = -1
    for number in list_of_integers:
        if number > highest_prime and isPrime(number):
            highest_prime = number

    digit_sum = 0
    s = str(highest_prime)
    for i in range(len(s)):
        digit_sum += int(s[i])

    return digit_sum