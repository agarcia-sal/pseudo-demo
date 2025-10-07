from typing import Tuple, Union


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(num: int) -> bool:
        if num in (0, 1):
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        divisor = 3
        while divisor * divisor <= num:
            if num % divisor == 0:
                return False
            divisor += 2
        return True

    leave_left, leave_right = interval1
    fetch_left, fetch_right = interval2

    begin_point = leave_left if leave_left > fetch_left else fetch_left
    end_point = leave_right if leave_right < fetch_right else fetch_right
    span = end_point - begin_point

    if span > 0 and is_prime(span):
        return "YES"
    return "NO"