from typing import Literal

def special_factorial(integer_n: int) -> int:
    factorial_of_i: int = 1
    special_factorial_result: int = 1
    for integer_i in range(1, integer_n + 1):
        factorial_of_i *= integer_i
        special_factorial_result *= factorial_of_i
    return special_factorial_result