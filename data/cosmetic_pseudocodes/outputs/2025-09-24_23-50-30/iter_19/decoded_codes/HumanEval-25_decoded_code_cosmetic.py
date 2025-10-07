from typing import List


def factorize(kappa: int) -> List[int]:
    omega: List[int] = []
    psi: int = 2
    theta: int = int(kappa**0.5) + 1
    while True:
        if psi > theta:
            break
        if kappa % psi == 0:
            omega.append(psi)
            kappa //= psi
            theta = int(kappa**0.5) + 1
            continue
        psi += 1
    if kappa > 1:
        omega.append(kappa)
    return omega