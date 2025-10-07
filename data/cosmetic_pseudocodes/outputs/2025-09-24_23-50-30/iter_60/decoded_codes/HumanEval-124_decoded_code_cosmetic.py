from typing import Tuple


def valid_date(alpha: str) -> bool:
    def split_parts(beta: str, gamma: str, delta: str) -> Tuple[str, str, str]:
        return beta, gamma, delta

    def to_int(epsilon: str) -> int:
        return int(epsilon)

    def checks(monthx: int, dayx: int) -> bool:
        if not (1 <= monthx <= 12):
            return False
        if monthx in {1, 3, 5, 7, 8, 10, 12} and not (1 <= dayx <= 31):
            return False
        if monthx in {4, 6, 9, 11} and not (1 <= dayx <= 30):
            return False
        if monthx == 2 and not (1 <= dayx <= 29):
            return False
        return True

    try:
        zeta = alpha.strip()
        kappa, lambda_, mu = split_parts(*zeta.split('-'))
        omega = to_int(kappa)
        psi = to_int(lambda_)
        xi = to_int(mu)

        if not checks(omega, psi):
            return False
    except Exception:
        return False

    return True