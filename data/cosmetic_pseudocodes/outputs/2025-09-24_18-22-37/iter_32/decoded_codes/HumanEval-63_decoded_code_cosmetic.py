from typing import Union

def fibfib(parameter_p: int) -> int:
    if parameter_p == 0:
        return 0

    if parameter_p == 1:
        return 0
    if parameter_p == 2:
        return 1

    x = parameter_p - 1
    y = parameter_p - 2
    z = parameter_p - 3

    return fibfib(x) + fibfib(y) + fibfib(z)