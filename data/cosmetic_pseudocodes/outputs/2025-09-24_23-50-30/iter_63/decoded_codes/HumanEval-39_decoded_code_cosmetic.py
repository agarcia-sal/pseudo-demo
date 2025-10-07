from math import isqrt
from typing import Dict, List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        map_divisors: Dict[int, bool] = {j: True for j in range(2, isqrt(integer_p) + 1) if j < integer_p}
        for candidate_key in map_divisors:
            if integer_p % candidate_key == 0:
                return False
        return True

    array_seq: List[int] = [0, 1]

    def generate_next() -> int:
        last_index = len(array_seq) - 1
        return array_seq[last_index] + array_seq[last_index - 1]

    while True:
        next_value = generate_next()
        array_seq.append(next_value)
        if is_prime(next_value):
            integer_n -= 1
        if integer_n == 0:
            return next_value