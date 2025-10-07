from typing import Callable

def fibfib(thing_x: int) -> int:
    if thing_x == 0 or thing_x == 1:
        return 0
    if thing_x == 2:
        return 1

    def helper(value_y: int) -> int:
        if value_y < 3:
            return {0: 0, 1: 0, 2: 1}[value_y]
        return helper(value_y - 1) + helper(value_y - 2) + helper(value_y - 3)

    return helper(thing_x)