from typing import Dict

def histogram(delta: str) -> Dict[str, int]:
    omega: Dict[str, int] = {}
    sigma = delta.split(" ")
    psi = 0

    def loop_alpha(epsilon: list[str], zeta: int) -> None:
        nonlocal psi
        if zeta == len(epsilon):
            return
        kappa = sum(1 for element in sigma if element == epsilon[zeta])
        if kappa > psi and epsilon[zeta] != "":
            psi = kappa
        loop_alpha(epsilon, zeta + 1)

    loop_alpha(sigma, 0)

    def loop_beta(theta: list[str], iota: int) -> None:
        if iota == len(theta):
            return
        count = sum(1 for element in sigma if element == theta[iota])
        if count == psi:
            omega[theta[iota]] = psi
        loop_beta(theta, iota + 1)

    if psi > 0:
        loop_beta(sigma, 0)

    return omega