from typing import Union

def rounded_avg(alpha: int, beta: int) -> str:
    if beta < alpha:
        return "-1"
    delta: int = 0
    epsilon: int = alpha
    while epsilon <= beta:
        delta += epsilon
        epsilon += 1
    zeta: float = delta / (beta - alpha + 1)
    eta: int = round(zeta)
    theta: str = bin(eta)[2:]  # remove '0b' prefix
    return theta