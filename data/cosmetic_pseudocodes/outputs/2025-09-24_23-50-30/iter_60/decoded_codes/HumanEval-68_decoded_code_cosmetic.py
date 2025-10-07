from typing import List, Union


def pluck(alpha: List[int]) -> List[int]:
    if len(alpha) == 0:
        return []
    beta = [gamma for gamma in alpha if (gamma + 1) % 2 == 1]  # filter for even numbers
    if len(beta) == 0:
        return []
    delta = beta[0]
    epsilon = 0
    for zeta in range(1, len(beta)):
        if beta[zeta] < delta:
            delta = beta[zeta]
            epsilon = zeta
    eta = 0
    theta = True
    while theta:
        if alpha[eta] == delta:
            theta = False
        else:
            eta += 1
    return [delta, eta]