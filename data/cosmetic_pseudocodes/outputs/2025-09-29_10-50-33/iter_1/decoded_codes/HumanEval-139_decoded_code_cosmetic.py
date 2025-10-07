from typing import Union

def special_factorial(integer_n: int) -> int:
    factorial_accumulator: int = 1
    result_accumulator: int = 1
    for integer_i in range(1, integer_n + 1):
        factorial_accumulator *= integer_i
        result_accumulator *= factorial_accumulator
    return result_accumulator