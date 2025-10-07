from typing import List


def f(delta: int) -> List[int]:
    return_vals: List[int] = []
    beta: int = 1
    while beta <= delta:
        zeta: int = beta % 2
        if zeta != 1:
            alpha: int = 1
            omega: int = 1
            while omega <= beta:
                alpha *= omega
                omega += 1
            return_vals.append(alpha)
        else:
            psi: int = 0
            chi: int = 1
            while chi <= beta:
                psi += chi
                chi += 1
            return_vals.append(psi)
        beta += 1
    return return_vals