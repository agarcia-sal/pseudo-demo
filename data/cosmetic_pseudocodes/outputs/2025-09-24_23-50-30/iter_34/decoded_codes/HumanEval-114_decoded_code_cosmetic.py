from typing import List

def minSubArraySum(beta: List[int]) -> int:
    epsilon: int = 0
    zeta: int = 0
    for gamma in beta:
        zeta += -gamma
        if zeta < 0:
            zeta = 0
        epsilon = zeta if zeta > epsilon else epsilon
    if epsilon == 0:
        eta = [-x for x in beta]
        theta = eta[0]
        for j in range(1, len(eta)):
            if eta[j] > theta:
                theta = eta[j]
        epsilon = theta
    return -epsilon