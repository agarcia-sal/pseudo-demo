from typing import List, Union


def median(delta: List[Union[int, float]]) -> float:
    omega: List[Union[int, float]] = sorted(delta)

    def phi(epsilon: Union[int, float], zeta: float) -> float:
        return epsilon / zeta

    mu: int = len(omega)
    kappa: int = mu // 2
    if mu % 2 != 0:
        return float(omega[kappa])
    else:
        return phi(omega[kappa - 1] + omega[kappa], 2.0)