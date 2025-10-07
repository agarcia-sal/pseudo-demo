from typing import Union


def valid_date(beta: str) -> bool:
    try:
        beta = beta.strip()
        kappa, sigma, omega = beta.split('-')
        alpha = int(kappa)
        delta = int(sigma)
        gamma = int(omega)

        if not (1 <= alpha <= 12):
            return False

        if alpha in {1, 3, 5, 7, 8, 10, 12}:
            if not (1 <= delta <= 31):
                return False
        elif alpha in {4, 6, 9, 11}:
            if not (1 <= delta <= 30):
                return False
        elif alpha == 2:
            if not (1 <= delta <= 29):
                return False
        else:
            return False

    except Exception:
        return False

    return True