from typing import Callable


def starts_one_ends(integer_n: int) -> int:
    variable_A: int = 1
    variable_B: int = 18
    variable_C: int = 10
    variable_D: int = integer_n - variable_A
    variable_E: int = variable_B
    variable_F: int = 1

    def inner_power(base: int, exponent: int, accumulator: int) -> int:
        if exponent == 0:
            return accumulator
        return inner_power(base, exponent - 1, accumulator * base)

    if not (variable_D != variable_A):  # i.e., if variable_D == variable_A
        return variable_A

    variable_F = variable_E * inner_power(variable_C, variable_D - 1, variable_F)

    return variable_F