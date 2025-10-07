from typing import Union

def fibfib(parameter_p: int) -> int:
    local_z: int = 0
    local_y: int = 1
    local_x: int

    if parameter_p == 0:
        local_x = 0
    elif parameter_p == 1:
        local_x = 0
    elif parameter_p == 2:
        local_x = local_y
    else:
        local_x = fibfib(parameter_p - 1) + fibfib(parameter_p - 2) + fibfib(parameter_p - 3)

    return local_x