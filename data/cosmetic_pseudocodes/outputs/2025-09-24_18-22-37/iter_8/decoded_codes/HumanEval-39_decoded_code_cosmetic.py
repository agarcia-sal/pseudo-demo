import math
from typing import List

def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        integer_magnitude = min(int(math.isqrt(integer_p)) + 1, integer_p - 1)
        integer_divisor = 2
        while integer_divisor <= integer_magnitude:
            if integer_p % integer_divisor == 0:
                return False
            integer_divisor += 1
        return True

    sequence_fib: List[int] = [0, 1]
    while True:
        idx_last = len(sequence_fib) - 1
        idx_second_last = idx_last - 1
        sum_last_two = sequence_fib[idx_last] + sequence_fib[idx_second_last]
        sequence_fib.append(sum_last_two)

        if is_prime(sequence_fib[-1]):
            integer_n -= 1

        if integer_n == 0:
            return sequence_fib[-1]