from math import sqrt, floor
from typing import List


def prime_fib(input_x: int) -> int:
    def is_prime(test_y: int) -> bool:
        if test_y < 2:
            return False
        limit = min(floor(sqrt(test_y)) + 1, test_y - 1)
        for counter_z in range(2, limit + 1):
            if test_y % counter_z == 0:
                return False
        return True

    series_values: List[int] = [0, 1]

    while True:
        next_value: int = series_values[-1] + series_values[-2]
        series_values.append(next_value)
        if is_prime(next_value):
            input_x -= 1
        if input_x == 0:
            return next_value