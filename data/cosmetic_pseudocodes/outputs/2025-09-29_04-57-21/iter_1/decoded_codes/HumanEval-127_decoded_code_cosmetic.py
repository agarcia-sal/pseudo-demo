from typing import Sequence

def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> str:
    def is_prime(number: int) -> bool:
        if number <= 1:
            return False
        if number == 2:
            return True
        for divisor in range(2, number):
            if number % divisor == 0:
                return False
        return True

    start_point = interval1[0]
    end_point = interval1[1]
    start_point2 = interval2[0]
    end_point2 = interval2[1]

    left_bound = start_point if start_point > start_point2 else start_point2
    right_bound = end_point if end_point < end_point2 else end_point2
    length = right_bound - left_bound

    if length > 0 and is_prime(length):
        return "YES"
    return "NO"