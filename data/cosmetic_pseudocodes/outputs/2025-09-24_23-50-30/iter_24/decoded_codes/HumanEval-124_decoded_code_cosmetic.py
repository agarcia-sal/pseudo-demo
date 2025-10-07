from typing import Union


def valid_date(alpha: str) -> bool:
    beta: str = alpha.strip()
    zeta: int = beta.find('-')
    eta: int = beta.rfind('-')
    if zeta < 0 or eta <= zeta:
        return False

    gamma: str = beta[:zeta]
    delta: str = beta[zeta + 1:eta]
    epsilon: str = beta[eta + 1:]

    try:
        lambda_: int = int(gamma)
        mu: int = int(delta)
        nu: int = int(epsilon)
    except ValueError:
        return False

    if not (1 <= lambda_ <= 12):
        return False
    if lambda_ in {1, 3, 5, 7, 8, 10, 12}:
        if not (1 <= mu <= 31):
            return False
    elif lambda_ in {4, 6, 9, 11}:
        if not (1 <= mu <= 30):
            return False
    elif lambda_ == 2:
        if not (1 <= mu <= 29):
            return False

    return True