from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number <= 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        divisor = 3
        while divisor * divisor <= number:
            if number % divisor == 0:
                return False
            divisor += 2
        return True

    a, c = interval1
    b, d = interval2

    lef = a if a > b else b
    rig = c if c < d else d

    diff = rig - lef
    if diff > 0 and is_prime(diff):
        return "YES"
    return "NO"