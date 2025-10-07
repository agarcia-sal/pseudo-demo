from typing import Union


def rounded_avg(alpha: int, beta: int) -> Union[int, str]:
    if beta < alpha:
        return -1
    omega = 0
    delta = alpha
    while delta <= beta:
        omega += delta
        delta += 1
    epsilon = omega / (beta - alpha + 1)
    zeta = round(epsilon)
    eta = bin(zeta)[2:]  # convert to binary string without '0b' prefix
    return eta