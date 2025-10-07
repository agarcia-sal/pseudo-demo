from typing import Literal

def fibfib(integer_n: int) -> int:
    match integer_n:
        case 0 | 1:
            return 0
        case 2:
            return 1
    alpha: int = integer_n
    beta: int = alpha - 1
    gamma: int = alpha - 2
    delta: int = alpha - 3
    sum1: int = fibfib(beta)
    sum2: int = fibfib(gamma)
    sum3: int = fibfib(delta)
    total: int = sum1 + sum2 + sum3
    return total