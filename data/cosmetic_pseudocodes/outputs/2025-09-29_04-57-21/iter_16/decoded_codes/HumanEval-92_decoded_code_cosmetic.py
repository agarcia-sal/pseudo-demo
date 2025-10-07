from typing import Any


def any_int(alpha: Any, beta: Any, gamma: Any) -> bool:
    if isinstance(alpha, int) and isinstance(beta, int) and isinstance(gamma, int):
        temp1 = (alpha + beta) == gamma
        temp2 = (alpha + gamma) == beta
        temp3 = (beta + gamma) == alpha
        return temp1 or temp2 or temp3
    return False