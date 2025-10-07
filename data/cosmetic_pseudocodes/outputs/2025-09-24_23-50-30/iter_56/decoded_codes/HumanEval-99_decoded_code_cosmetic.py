from math import floor, ceil
from typing import Union


def closest_integer(parameter_alpha: str) -> int:
    def remove_trailing_zeros(param_beta: str) -> str:
        # Remove trailing zeros recursively if last char is '0'
        if not param_beta or param_beta[-1] != '0':
            return param_beta
        return remove_trailing_zeros(param_beta[:-1])

    count_dot = 0

    def count_dots(param_gamma: str, param_delta: int) -> int:
        nonlocal count_dot
        if param_delta == len(param_gamma):
            return count_dot
        if param_gamma[param_delta] == '.':
            count_dot += 1
        return count_dots(param_gamma, param_delta + 1)

    count_dot = count_dots(parameter_alpha, 0)

    if count_dot == 1:
        parameter_alpha = remove_trailing_zeros(parameter_alpha)

    variable_theta = float(parameter_alpha) if parameter_alpha else 0.0
    variable_omicron = 0

    if len(parameter_alpha) >= 2 and parameter_alpha[-2:] == '.5':
        if variable_theta > 0:
            variable_omicron = ceil(variable_theta)
        else:
            variable_omicron = floor(variable_theta)
    elif len(parameter_alpha) > 0:
        def sign(x: float) -> int:
            return (x > 0) - (x < 0)
        variable_omicron = int(variable_theta + 0.5 * sign(variable_theta))
    else:
        variable_omicron = 0

    return variable_omicron