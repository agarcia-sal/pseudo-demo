from typing import Union

def fib(parameter_alpha: int) -> int:
    if parameter_alpha == 0:
        return 0
    elif parameter_alpha == 1:
        return 1
    else:
        temp_beta: int = parameter_alpha - 1
        temp_gamma: int = parameter_alpha - 2
        result_delta: int = fib(temp_beta) + fib(temp_gamma)
        return result_delta