from functools import cache

@cache
def fibfib(number_z: int) -> int:
    if number_z == 0:
        return 0
    if number_z == 1:
        return 0
    if number_z == 2:
        return 1
    return fibfib(number_z - 1) + fibfib(number_z - 2) + fibfib(number_z - 3)