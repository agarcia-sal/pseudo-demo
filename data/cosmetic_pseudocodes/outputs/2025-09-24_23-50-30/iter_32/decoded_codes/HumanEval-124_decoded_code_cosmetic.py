from typing import Any


def valid_date(alpha: str) -> bool:
    try:
        zeta = alpha.strip()
        kappa, psi, omega = zeta.split('-')
        epsilon = int(kappa)
        delta = int(psi)
        gamma = int(omega)

        if not (1 <= epsilon <= 12):
            return False

        if epsilon in {1, 3, 5, 7, 8, 10, 12}:
            if delta < 1 or delta > 31:
                return False
        elif epsilon in {4, 6, 9, 11}:
            if delta < 1 or delta > 30:
                return False
        elif epsilon == 2:
            if delta < 1 or delta > 29:
                return False
        # default case needs no action

    except Exception:  # catch any exception
        return False

    return True