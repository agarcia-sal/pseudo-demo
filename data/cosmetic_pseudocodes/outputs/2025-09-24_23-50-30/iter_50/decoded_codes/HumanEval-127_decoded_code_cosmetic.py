from typing import Tuple, Union


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(input_val: int) -> bool:
        def check_divisor_divisible(val: int, current: int) -> bool:
            if current >= val:
                return True
            if val % current == 0:
                return False
            return check_divisor_divisible(val, current + 1)

        if input_val in (0, 1):
            return False
        if input_val == 2:
            return True
        return check_divisor_divisible(input_val, 2)

    lower_bound = interval1[0] if interval1[0] >= interval2[0] else interval2[0]
    upper_bound = interval1[1] if interval1[1] <= interval2[1] else interval2[1]
    length_of_intersection = upper_bound - lower_bound

    if length_of_intersection > 0 and is_prime(length_of_intersection):
        return "YES"
    return "NO"