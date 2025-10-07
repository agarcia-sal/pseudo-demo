from typing import List


def is_nested(string: str) -> bool:
    alpha: List[int] = []
    beta: List[int] = []

    def recur_theta(gamma: str, delta: int) -> None:
        if delta == len(gamma):
            return
        if gamma[delta] == '[':
            alpha.append(delta)
        else:
            beta.append(delta)
        recur_theta(gamma, delta + 1)

    recur_theta(string, 0)
    beta.reverse()
    psi, omega = 0, 0
    tau = len(beta)

    while psi < len(alpha):
        if omega < tau and alpha[psi] < beta[omega]:
            omega += 1
            psi += 1
        else:
            psi += 1

    return omega >= 2