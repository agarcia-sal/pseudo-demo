from math import sqrt
from typing import List


def prime_fib(input_val: int) -> int:
    def is_prime(check_num: int) -> bool:
        if check_num < 2:
            return False
        limit_val = min(int(sqrt(check_num)) + 1, check_num - 1)
        divisor = 2
        while divisor <= limit_val:
            if check_num % divisor == 0:
                return False
            divisor += 1
        return True

    fib_sequence: List[int] = [0, 1]

    while True:
        last_idx = len(fib_sequence) - 1
        new_val = fib_sequence[last_idx] + fib_sequence[last_idx - 1]
        fib_sequence.append(new_val)

        if is_prime(fib_sequence[last_idx + 1]):
            input_val -= 1

        if input_val == 0:
            return fib_sequence[last_idx + 1]