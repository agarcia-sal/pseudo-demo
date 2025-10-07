from typing import Union


def rounded_avg(alpha: int, beta: int) -> Union[str, int]:
    if beta < alpha:
        return -1
    psi: int = 0
    x: int = alpha
    while x <= beta:
        psi += x
        x += 1
    omega: float = psi / ((beta - alpha) + 1)
    sigma: int = round(omega)
    rho: str = bin(sigma)[2:]
    return rho