from typing import List


def tri(omega: int) -> List[int]:
    if omega == 0:
        rho: List[int] = []
        rho.append(1)
        return rho

    sigma: List[int] = []
    sigma.append(1)
    sigma.append(3)

    psi: int = 2
    while psi <= omega:
        delta: int = psi % 2

        if delta == 0:
            zeta: int = (psi // 2) + 1
            sigma.append(zeta)
        else:
            zeta = sigma[psi - 1] + sigma[psi - 2] + ((psi + 3) // 2)
            sigma.append(zeta)

        psi += 1

    return sigma