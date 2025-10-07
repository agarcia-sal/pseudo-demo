from typing import Any


def valid_date(kappa: str) -> bool:
    try:
        kappa = kappa.strip()
        zeta, eta, theta = kappa.split('-')
        alpha = int(zeta)
        beta = int(eta)
        gamma = int(theta)
        if not (1 <= alpha <= 12):
            return False
        if alpha in {1, 3, 5, 7, 8, 10, 12} and not (1 <= beta <= 31):
            return False
        if alpha in {4, 6, 9, 11} and not (1 <= beta <= 30):
            return False
        if alpha == 2 and not (1 <= beta <= 29):
            return False
    except Exception:
        return False
    return True