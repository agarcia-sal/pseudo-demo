from math import sqrt, floor
from typing import List


def skjkasdkd(array_of_numbers: List[int]) -> int:
    def isPrime(number: int) -> bool:
        if number < 2:
            return False
        limit = floor(sqrt(number)) + 1
        counter = 2
        while counter < limit:
            if number % counter == 0:
                return False
            counter += 1
        return True

    highest_prime: int = 0
    pos: int = 0
    length = len(array_of_numbers)
    while pos < length:
        val = array_of_numbers[pos]
        if val > highest_prime and isPrime(val):
            highest_prime = val
        pos += 1

    def sumDigits(str_value: str, acc: int, idx: int) -> int:
        if idx == len(str_value):
            return acc
        return sumDigits(str_value, acc + int(str_value[idx]), idx + 1)

    return sumDigits(str(highest_prime), 0, 0)