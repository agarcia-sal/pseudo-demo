from math import sqrt, floor
from typing import List


def prime_fib(n_counter: int) -> int:
    def is_prime(x_candidate: int) -> bool:
        if x_candidate < 2:
            return False
        limit_bound = floor(sqrt(x_candidate)) + 1
        max_check = min(limit_bound, x_candidate - 1)
        divisor = 2
        while divisor <= max_check:
            if x_candidate % divisor == 0:
                return False
            divisor += 1
        return True

    fibonacci_seq: List[int] = [0, 1]

    while True:
        last_idx = len(fibonacci_seq) - 1
        second_last_idx = last_idx - 1

        new_element = fibonacci_seq[second_last_idx] + fibonacci_seq[last_idx]
        fibonacci_seq.append(new_element)

        if is_prime(new_element):
            n_counter -= 1

        if n_counter == 0:
            return new_element