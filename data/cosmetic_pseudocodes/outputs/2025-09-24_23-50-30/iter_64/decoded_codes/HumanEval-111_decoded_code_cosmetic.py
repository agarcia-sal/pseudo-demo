from typing import Dict


def histogram(beta: str) -> Dict[str, int]:
    gamma: Dict[str, int] = {}
    delta = beta.split(" ")
    epsilon = 0

    def zeta(eta: int, theta: list[str], i: int) -> None:
        if i == len(theta):
            return
        if theta[i] != "" and theta.count(theta[i]) > eta:
            nonlocal epsilon
            epsilon = theta.count(theta[i])
        zeta(eta, theta, i + 1)

    zeta(epsilon, delta, 0)
    epsilon = epsilon or 0

    if epsilon > 0:
        for i in range(len(delta)):
            if delta.count(delta[i]) == epsilon:
                gamma[delta[i]] = epsilon

    return gamma