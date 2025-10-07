from typing import Union


def valid_date(alpha: str) -> bool:
    try:
        beta = alpha.strip()
        gamma, delta, epsilon = beta.split('-')
        zeta = int(gamma)
        eta = int(delta)
        theta = int(epsilon)

        if zeta < 1 or zeta > 12:
            return False
        if zeta in {1, 3, 5, 7, 8, 10, 12} and (eta < 1 or eta > 31):
            return False
        if zeta in {4, 6, 9, 11} and (eta < 1 or eta > 30):
            return False
        if zeta == 2 and (eta < 1 or eta > 29):
            return False
    except Exception:
        return False
    return True