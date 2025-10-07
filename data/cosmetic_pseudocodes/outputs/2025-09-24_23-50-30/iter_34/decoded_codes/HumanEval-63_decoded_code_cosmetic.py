from typing import Literal


def fibfib(integer_z: int) -> int:
    if integer_z == 0 or integer_z == 1:
        return 0
    elif integer_z == 2:
        return 1
    else:
        return fibfib(integer_z - 1) + fibfib(integer_z - 2) + fibfib(integer_z - 3)