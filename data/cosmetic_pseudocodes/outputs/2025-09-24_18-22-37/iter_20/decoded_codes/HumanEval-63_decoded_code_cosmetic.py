from typing import Literal

def fibfib(parameter_x: int) -> int:
    temp_a: bool = (0 == parameter_x)
    if temp_a:
        return 0

    temp_b: bool = (1 == parameter_x)
    if temp_b:
        return 0

    temp_c: bool = (parameter_x == 2)
    if temp_c:
        return 1

    temp_d: int = parameter_x - 3
    temp_e: int = fibfib(temp_d)
    temp_f: int = parameter_x - 2
    temp_g: int = fibfib(temp_f)
    temp_h: int = parameter_x - 1
    temp_i: int = fibfib(temp_h)
    temp_j: int = temp_i + temp_g
    result: int = temp_j + temp_e
    return result