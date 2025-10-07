from typing import Literal


def fibfib(parameter_x: int) -> int:
    if parameter_x == 0:
        return 0
    elif parameter_x == 1:
        return 0
    elif parameter_x == 2:
        return 1
    else:
        intermediate_y: int = parameter_x - 1
        intermediate_z: int = parameter_x - 2
        intermediate_w: int = parameter_x - 3
        return fibfib(intermediate_y) + fibfib(intermediate_z) + fibfib(intermediate_w)