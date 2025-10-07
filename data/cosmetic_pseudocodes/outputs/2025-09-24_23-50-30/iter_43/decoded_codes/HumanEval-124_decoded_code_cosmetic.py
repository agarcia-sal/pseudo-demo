from typing import Optional


def valid_date(beta: str) -> bool:
    try:
        beta = beta.strip()
        gamma = beta.split('-')
        delta = int(gamma[0])
        epsilon = int(gamma[1])
        zeta = int(gamma[2])

        if delta <= 0 or delta > 12:
            return False
        if delta in {1, 3, 5, 7, 8, 10, 12} and (epsilon <= 0 or epsilon > 31):
            return False
        if delta in {4, 6, 9, 11} and (epsilon <= 0 or epsilon > 30):
            return False
        if delta == 2 and (epsilon <= 0 or epsilon > 29):
            return False
    except Exception:
        return False

    return True