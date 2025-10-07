from typing import Literal

def fibfib(arg_x: int) -> int:
    if arg_x == 0:
        return 0
    elif arg_x == 1:
        return 0
    elif arg_x == 2:
        return 1
    else:
        return fibfib(arg_x - 1) + fibfib(arg_x - 2) + fibfib(arg_x - 3)