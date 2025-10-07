from typing import Callable

def choose_num(x: int, y: int) -> int:
    # Evaluate the conditions
    condition1: bool = (x > y)
    condition2: bool = (y % 2 == 0)
    condition3: bool = (x == y)

    # DECIDE logic following the pseudocode
    if not condition1:
        return -1
    if condition2:
        return y
    if not condition3:
        return -1

    return y - 1