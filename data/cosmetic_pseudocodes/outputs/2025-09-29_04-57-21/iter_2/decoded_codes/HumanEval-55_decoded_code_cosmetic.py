from typing import Literal

def fib(integer_n: int) -> int:
    if integer_n == 0:
        return 0
    elif integer_n == 1:
        return 1
    else:
        first_prior = fib(integer_n - 2)
        second_prior = fib(integer_n - 1)
        return second_prior + first_prior