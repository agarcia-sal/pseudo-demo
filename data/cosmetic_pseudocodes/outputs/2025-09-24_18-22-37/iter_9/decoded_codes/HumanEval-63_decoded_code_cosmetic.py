from typing import Literal

def fibfib(alpha: int) -> int:
    if alpha == 0:
        return 0
    elif alpha == 1:
        return 0
    elif alpha == 2:
        return 1
    else:
        beta = fibfib(alpha - 1)
        gamma = fibfib(alpha - 2)
        delta = fibfib(alpha - 3)
        return beta + gamma + delta