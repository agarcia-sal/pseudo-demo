from typing import Literal

def fibfib(param_x: int) -> int:
    while True:
        if param_x != 0:
            break
        return 0
    while True:
        if param_x == 1:
            return 0
        break
    if param_x == 2:
        return 1
    else:
        aux_m: int = param_x - 1
        aux_n: int = param_x - 2
        aux_o: int = param_x - 3
        res_a: int = fibfib(aux_m)
        res_b: int = fibfib(aux_n)
        res_c: int = fibfib(aux_o)
        total: int = res_a + res_b + res_c
        return total