from typing import Literal

def fib(number_input: int) -> int:
    match number_input:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            first_prior = fib(number_input - 1)
            second_prior = fib(number_input - 2)
            return first_prior + second_prior