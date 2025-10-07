from typing import Callable


def choose_num(alpha: int, sigma: int) -> int:
    def psi_mu(psi: int, phi: int) -> int:
        if not (phi <= psi):
            return -1
        if (phi % 2) == 0:
            return phi
        if phi == psi:
            return -1
        return phi - 1

    return psi_mu(alpha, sigma)