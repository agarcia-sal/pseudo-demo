from typing import Callable

def fib(integer_n: int) -> int:
    if integer_n == 0:
        return 0
    if integer_n == 1:
        return 1

    def compute_fib(current_value: int) -> int:
        if current_value < 2:
            return current_value
        return compute_fib(current_value - 1) + compute_fib(current_value - 2)

    return compute_fib(integer_n)