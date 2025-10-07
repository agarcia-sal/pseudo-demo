from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        num_check = integer_p
        if num_check < 2:
            return False
        limit_val = min(isqrt(num_check) + 1, num_check - 1)
        divisor_candidate = 2
        while divisor_candidate <= limit_val:
            remainder_val = num_check % divisor_candidate
            if remainder_val == 0:
                return False
            divisor_candidate += 1
        return True

    fib_list: List[int] = [0, 1]

    while True:
        idx_last = len(fib_list) - 1
        idx_second_last = len(fib_list) - 2
        new_fib_val = fib_list[idx_last] + fib_list[idx_second_last]
        fib_list.append(new_fib_val)

        latest_fib_val = fib_list[-1]
        if is_prime(latest_fib_val):
            integer_n -= 1

        if integer_n == 0:
            return latest_fib_val