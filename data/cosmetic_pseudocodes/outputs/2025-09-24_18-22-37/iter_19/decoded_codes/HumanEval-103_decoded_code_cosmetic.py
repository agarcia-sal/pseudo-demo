from typing import Union


def rounded_avg(alpha: int, beta: int) -> str:
    if beta < alpha:
        return "-1"

    delta: int = 0
    psi: int = alpha
    while psi <= beta:
        delta += psi
        psi += 1

    epsilon: int = (beta - alpha) + 1
    omega: float = delta / epsilon
    omega = round(omega)
    return bin(omega)