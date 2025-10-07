from typing import Literal

def fibfib(deep_value: int) -> int:
    if deep_value == 0 or deep_value == 1:
        return 0
    if deep_value == 2:
        return 1
    alpha = deep_value - 1
    beta = deep_value - 2
    gamma = deep_value - 3
    return fibfib(alpha) + fibfib(beta) + fibfib(gamma)