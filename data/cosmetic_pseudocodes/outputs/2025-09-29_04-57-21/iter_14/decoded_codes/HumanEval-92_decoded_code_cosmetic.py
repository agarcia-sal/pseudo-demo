from typing import Any


def any_int(alpha: Any, beta: Any, gamma: Any) -> bool:
    if not isinstance(alpha, int):
        return False
    if not isinstance(beta, int):
        return False
    if not isinstance(gamma, int):
        return False

    temp1 = alpha + beta
    temp2 = alpha + gamma
    temp3 = beta + gamma

    if temp1 == gamma:
        return True
    if temp2 == beta:
        return True
    if temp3 == alpha:
        return True

    return False