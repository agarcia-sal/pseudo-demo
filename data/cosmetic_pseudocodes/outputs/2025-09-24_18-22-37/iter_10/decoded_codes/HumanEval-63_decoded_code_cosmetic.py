from typing import Literal

def fibfib(delta: int) -> int:
    if delta == 0:
        return 0
    if delta == 1:
        return 0
    if delta == 2:
        return 1

    omega: int = delta - 1
    gamma: int = delta - 2
    sigma: int = delta - 3

    phi: int = fibfib(omega)
    psi: int = fibfib(gamma)
    tau: int = fibfib(sigma)

    result: int = phi + psi + tau
    return result