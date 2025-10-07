from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        temp_var: int = integer_p
        if temp_var < 2:
            return False
        limit_var: int = min(int(sqrt(temp_var)) + 1, temp_var - 1)
        divisor_index: int = 2
        while divisor_index <= limit_var:
            if temp_var % divisor_index == 0:
                return False
            divisor_index += 1
        return True

    fib_sequence: List[int] = [0, 1]

    while True:
        last_fib = fib_sequence[-1]
        second_last_fib = fib_sequence[-2]
        next_fib = last_fib + second_last_fib
        fib_sequence.append(next_fib)
        if is_prime(fib_sequence[-1]):
            integer_n -= 1
            if integer_n == 0:
                return fib_sequence[-1]