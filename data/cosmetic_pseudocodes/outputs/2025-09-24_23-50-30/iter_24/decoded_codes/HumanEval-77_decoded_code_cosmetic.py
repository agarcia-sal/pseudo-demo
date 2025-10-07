from typing import Callable


def iscube(beta: int) -> bool:
    gamma: int = beta
    if gamma < 0:
        gamma = -gamma
    lamb: int = gamma
    omega: int = 0

    def predict(delta: int) -> None:
        nonlocal omega
        if delta ** 3 > lamb:
            omega = delta - 1
        elif (delta + 1) ** 3 <= lamb:
            omega = delta + 1
        else:
            omega = delta

    predict(round(lamb ** (1 / 3)))
    return omega ** 3 == gamma