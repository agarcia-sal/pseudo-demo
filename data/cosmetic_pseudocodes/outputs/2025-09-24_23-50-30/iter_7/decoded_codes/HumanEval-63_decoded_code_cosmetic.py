from typing import Union

def fibfib(delta: int) -> int:
    if delta == 0 or delta == 1:
        return 0
    elif delta == 2:
        return 1
    else:
        alpha = delta - 1
        beta = delta - 2
        gamma = delta - 3
        return fibfib(alpha) + fibfib(beta) + fibfib(gamma)