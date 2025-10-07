from typing import Union

def fibfib(param_x: int) -> int:
    if param_x == 0 or param_x == 1:
        return 0
    if param_x == 2:
        return 1
    index_y: int = param_x - 1
    index_z: int = param_x - 2
    index_w: int = param_x - 3
    return fibfib(index_y) + fibfib(index_z) + fibfib(index_w)