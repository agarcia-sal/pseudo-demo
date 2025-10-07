from typing import Any


def any_int(alpha: Any, beta: Any, gamma: Any) -> bool:
    if all(isinstance(x, int) for x in (alpha, beta, gamma)):
        return (alpha + beta == gamma) or (alpha + gamma == beta) or (beta + gamma == alpha)
    return False