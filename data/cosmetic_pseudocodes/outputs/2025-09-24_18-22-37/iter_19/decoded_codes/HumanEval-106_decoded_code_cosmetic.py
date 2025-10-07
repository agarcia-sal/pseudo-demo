from typing import List

def f(kappa: int) -> List[int]:
    omega: List[int] = []
    psi: int = 1
    sigma: int = 0
    chi: int = 0

    for _ in range(kappa):
        chi += 1
        if chi % 2 == 0:  # even chi
            psi = 1
            zeta = 1
            while zeta <= chi:
                psi *= zeta
                zeta += 1
            omega.append(psi)
        else:  # odd chi
            sigma = 0
            for alpha in range(1, chi + 1):
                sigma += alpha
            omega.append(sigma)

    return omega