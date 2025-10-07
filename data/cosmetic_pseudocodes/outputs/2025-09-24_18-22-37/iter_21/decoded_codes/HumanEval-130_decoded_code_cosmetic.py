from typing import List

def tri(alpha: int) -> List[int]:
    if alpha == 0:
        return [1]

    omega: List[int] = [1, 3]
    sigma: int = 2
    while sigma <= alpha:
        if sigma % 2 == 0:
            psi = sigma // 2 + 1
            omega.append(psi)
        else:
            chi = omega[sigma - 1]
            phi = omega[sigma - 2]
            theta = (sigma + 3) // 2
            epsilon = chi + phi + theta
            omega.append(epsilon)
        sigma += 1

    return omega