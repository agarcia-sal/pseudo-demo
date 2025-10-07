from math import floor, sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        upper_bound = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
        for idx in range(2, upper_bound + 1):
            if integer_p % idx == 0:
                return False
        return True

    sequence_list: List[int] = [0, 1]

    while True:
        next_val = sequence_list[-1] + sequence_list[-2]
        sequence_list.append(next_val)

        if is_prime(sequence_list[-1]):
            integer_n -= 1

        if integer_n == 0:
            return sequence_list[-1]