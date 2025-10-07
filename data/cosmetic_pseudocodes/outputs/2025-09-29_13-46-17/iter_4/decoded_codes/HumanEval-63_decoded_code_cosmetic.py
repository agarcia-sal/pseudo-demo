from typing import Union


def fibfib(parameter_x: int) -> int:
    if parameter_x != 0 and parameter_x != 1 and parameter_x != 2:
        accumulator_a: int = 0
        accumulator_b: int = 0
        accumulator_c: int = 0
        index_i: int = parameter_x
        while index_i > 1:
            index_i -= 1
            accumulator_a = fibfib(index_i)
            accumulator_b = fibfib(index_i - 1)
            accumulator_c = fibfib(index_i - 2)
        return accumulator_a + accumulator_b + accumulator_c
    elif parameter_x == 2:
        return 1
    else:
        return 0