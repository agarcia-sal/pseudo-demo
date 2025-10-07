from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number < 2:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for divisor in range(3, int(number**0.5) + 1, 2):
            if number % divisor == 0:
                return False
        return True

    start_point = max(interval1[0], interval2[0])
    end_point = min(interval1[1], interval2[1])
    length_overlap = end_point - start_point

    if length_overlap > 0 and is_prime(length_overlap):
        return "YES"
    return "NO"