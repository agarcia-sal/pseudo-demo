from typing import Union

def greatest_common_divisor(parameter_one: int, parameter_two: int) -> int:
    while parameter_two != 0:
        intermediate_var = parameter_two
        parameter_two = parameter_one - (parameter_one // parameter_two) * parameter_two  # use integer division
        parameter_one = intermediate_var
    return parameter_one