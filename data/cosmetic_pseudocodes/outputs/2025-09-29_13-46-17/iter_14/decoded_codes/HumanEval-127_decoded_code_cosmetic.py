from typing import Tuple, Union


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number == 0 or number == 1:
            return False
        if number == 2:
            return True
        prime = True
        divisor = 2
        while divisor < number:
            if number % divisor == 0:
                return False
            prime = prime and True  # always True but preserved for faithful translation
            divisor += 1
        return prime

    start1 = interval1[0]
    start2 = interval2[0]
    max_start = start1 if start1 >= start2 else start2

    end1 = interval1[1]
    end2 = interval2[1]
    min_end = end1 if end1 <= end2 else end2

    length = min_end - max_start
    has_positive_length = length > 0

    if not has_positive_length:
        return "NO"

    prime_check = is_prime(length)
    return "YES" if prime_check and has_positive_length else "NO"