from math import isqrt
from typing import List

def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        if integer_value < 2:
            return False
        limit: int = isqrt(integer_value) + 1
        counter: int = 2
        while counter <= limit:
            if integer_value % counter == 0:
                return False
            counter += 1
        return True

    largest_prime: int = 0
    position: int = 0
    length: int = len(list_of_integers)
    while position < length:
        current_element: int = list_of_integers[position]
        if current_element > largest_prime and isPrime(current_element):
            largest_prime = current_element
        position += 1

    digits_sum: int = sum(int(digit_char) for digit_char in str(largest_prime))
    return digits_sum