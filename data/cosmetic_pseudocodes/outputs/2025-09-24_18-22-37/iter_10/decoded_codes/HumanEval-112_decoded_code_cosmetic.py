from typing import Tuple

def reverse_delete(parameter_x: str, parameter_y: str) -> Tuple[str, bool]:
    variable_a = ''
    variable_b = 0
    while variable_b < len(parameter_x):
        variable_c = parameter_x[variable_b]
        if variable_c not in parameter_y:
            variable_a += variable_c
        variable_b += 1

    variable_d = ''
    variable_e = len(variable_a) - 1
    while variable_e >= 0:
        variable_d += variable_a[variable_e]
        variable_e -= 1

    variable_f = (variable_d == variable_a)

    return variable_a, variable_f