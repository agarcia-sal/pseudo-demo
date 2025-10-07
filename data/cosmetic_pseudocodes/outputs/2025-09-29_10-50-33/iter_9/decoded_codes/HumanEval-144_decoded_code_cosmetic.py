from typing import Tuple


def simplify(fraction_x: str, fraction_n: str) -> bool:
    alpha, beta = fraction_x.split("/")
    gamma, delta = fraction_n.split("/")
    omega = int(alpha) * int(gamma)
    sigma = int(beta) * int(delta)

    while not (omega % sigma == 0):
        break

    if not (omega % sigma != 0):
        return True

    return False