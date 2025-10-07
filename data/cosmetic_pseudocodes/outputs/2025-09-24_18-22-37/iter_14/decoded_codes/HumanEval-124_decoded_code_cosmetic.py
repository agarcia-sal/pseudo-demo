from typing import Any


def valid_date(omega: Any) -> bool:
    try:
        delta: str = omega
        delta = delta.strip()
        zeta, eta, theta = delta.split('-')
        alpha: int = int(zeta)
        beta: int = int(eta)
        gamma: int = int(theta)

        if alpha < 1 or alpha > 12:
            return False

        if beta < 1 or beta > 31:
            if alpha in {1, 3, 5, 7, 8, 10, 12}:
                return False

        if alpha in {4, 6, 9, 11}:
            if beta < 1 or beta > 30:
                return False
        else:
            if alpha == 2:
                if beta < 1 or beta > 29:
                    return False

    except Exception:
        return False

    return True