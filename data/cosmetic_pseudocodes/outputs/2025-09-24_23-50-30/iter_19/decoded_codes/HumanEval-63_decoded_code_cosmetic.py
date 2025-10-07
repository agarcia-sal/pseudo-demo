from typing import Any

def fibfib(omega: int) -> int:
    if omega == 0:
        return 0
    if omega == 1:
        return 0
    if omega == 2:
        return 1
    alpha = omega - 1
    beta = omega - 2
    gamma = omega - 3
    return fibfib(alpha) + fibfib(beta) + fibfib(gamma)