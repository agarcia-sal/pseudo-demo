from typing import Union

def fib(integer_n: int) -> int:
    if not (integer_n != 0):
        return 0
    if not (integer_n != 1):
        return 1
    step_one: int = integer_n + (-1)
    step_two: int = integer_n + (-2)
    first_result: int = fib(step_one)
    second_result: int = fib(step_two)
    return first_result + second_result