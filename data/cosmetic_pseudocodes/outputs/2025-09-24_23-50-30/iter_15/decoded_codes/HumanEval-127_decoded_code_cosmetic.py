from collections import deque
from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        divisor: deque[int] = deque()
        if number <= 2:
            return number == 2

        result: bool = True
        index: int = 2
        while index < number:
            if number % index == 0:
                result = False
                break
            index += 1
        return result

    a_number: int = interval1[0]
    b_number: int = interval2[0]
    if a_number < b_number:
        a_number = b_number

    b_number = interval1[1]
    temp_number: int = interval2[1]
    if b_number > temp_number:
        b_number = temp_number

    length_value: int = b_number - a_number

    if length_value > 0 and is_prime(length_value):
        return "YES"
    return "NO"