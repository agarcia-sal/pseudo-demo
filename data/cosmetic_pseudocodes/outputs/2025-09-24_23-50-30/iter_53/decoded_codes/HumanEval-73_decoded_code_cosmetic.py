from typing import Sequence, TypeVar

T = TypeVar('T')

def smallest_change(omega: Sequence[T]) -> int:
    alpha: int = 0
    gamma: int = len(omega)
    delta: int = gamma // 2
    kappa: int = 0
    while kappa < delta:
        mu = omega[kappa]
        nu = omega[gamma - kappa - 1]
        if mu != nu:
            alpha += 1
        kappa += 1
    return alpha