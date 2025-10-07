from typing import Literal

def fibfib(kappa: int) -> int:
    if kappa == 0 or kappa == 1:
        return 0
    if kappa == 2:
        return 1
    return fibfib(kappa - 1) + fibfib(kappa - 2) + fibfib(kappa - 3)