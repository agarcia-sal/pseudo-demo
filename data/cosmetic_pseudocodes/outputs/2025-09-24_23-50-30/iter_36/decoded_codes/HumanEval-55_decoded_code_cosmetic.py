from typing import Union

def fib(input_value: int) -> int:
    if input_value == 0:
        return 0
    elif input_value == 1:
        return 1
    else:
        alpha = input_value - 1
        beta = input_value - 2
        gamma = fib(alpha)
        delta = fib(beta)
        return gamma + delta