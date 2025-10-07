from typing import Optional


def valid_date(alpha: str) -> bool:
    try:
        alpha = alpha.strip()
        beta, gamma, delta = alpha.split('-')
        epsilon = int(beta)
        zeta = int(gamma)
        eta = int(delta)
        if epsilon < 1 or epsilon > 12:
            return False
        if epsilon in {1, 3, 5, 7, 8, 10, 12} and (zeta < 1 or zeta > 31):
            return False
        if epsilon in {4, 6, 9, 11} and (zeta < 1 or zeta > 30):
            return False
        if epsilon == 2 and (zeta < 1 or zeta > 29):
            return False
    except Exception:
        return False
    return True