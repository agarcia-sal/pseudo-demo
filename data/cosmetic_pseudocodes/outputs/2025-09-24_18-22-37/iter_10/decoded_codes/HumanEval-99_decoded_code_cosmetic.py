from math import floor, ceil
from typing import Union


def closest_integer(parameter_A: str) -> int:
    if parameter_A.count('.') == 1:
        while parameter_A and parameter_A[-1] == '0':
            parameter_A = parameter_A[:-1]

    variable_C = float(parameter_A)

    if parameter_A[-2:] == '.5':
        if variable_C > 0:
            variable_D = ceil(variable_C)
        else:
            variable_D = floor(variable_C)
    else:
        if len(parameter_A) > 0:
            variable_D = round(variable_C)
        else:
            variable_D = 0

    return variable_D