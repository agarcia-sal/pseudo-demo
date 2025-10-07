from typing import Literal

def fibfib(beta: int) -> int:
    if beta == 0:
        return 0
    elif beta == 1:
        return 0
    elif beta == 2:
        return 1
    else:
        omega = beta - 1
        sigma = beta - 2
        kappa = beta - 3
        return fibfib(omega) + fibfib(sigma) + fibfib(kappa)