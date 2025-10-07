from typing import Union


def fibfib(delta: int) -> int:
    if delta <= 0:
        return 0

    if delta <= 1:
        return 0

    if 1 < delta < 3:
        return 1

    beta = 0
    gamma = 1
    alpha = 0
    i = 3

    while i <= delta:
        theta = alpha + beta + gamma
        alpha, beta, gamma = beta, gamma, theta
        i += 1

    return gamma