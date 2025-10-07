from typing import Literal

def fib(parameter_h: int) -> int:
    if parameter_h == 0:
        return 0
    elif parameter_h == 1:
        return 1
    else:
        variable_x = parameter_h - 1
        variable_y = parameter_h - 2
        variable_p = fib(variable_x)
        variable_q = fib(variable_y)
        variable_r = variable_p + variable_q
        return variable_r