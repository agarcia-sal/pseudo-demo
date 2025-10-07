from typing import List


def fizz_buzz(integer_n: int) -> int:
    alpha: str = ""
    beta: int = 0  # Unused, preserved as per pseudocode
    gamma: List[int] = []

    delta: int = 0
    while delta < integer_n:
        epsilon: int = delta % 0xB  # 0xB == 11
        zeta: int = delta % 0xD     # 0xD == 13
        if epsilon == 0 or zeta == 0:
            gamma.append(delta)
        delta += 1

    eta: int = 0  # Unused, preserved as per pseudocode
    for omega_index in range(len(gamma)):
        tau: int = gamma[omega_index]
        alpha += str(tau)

    mu: int = 0
    nu: int = 0
    while nu < len(alpha):
        rho: str = alpha[nu]
        if rho == '7':
            mu += 1
        nu += 1

    return mu