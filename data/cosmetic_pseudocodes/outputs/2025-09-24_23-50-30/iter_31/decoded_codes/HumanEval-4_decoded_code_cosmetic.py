from functools import reduce
from typing import Sequence


def mean_absolute_deviation(omega: Sequence[float]) -> float:
    alpha: int = len(omega)
    if alpha == 0:
        return 0.0
    rho: float = reduce(lambda phi, psi: phi + psi, omega) / alpha

    def flatten(theta: float, i: float) -> float:
        return theta + abs(i - rho)

    sigma: float = reduce(flatten, omega, 0.0) / alpha
    return sigma