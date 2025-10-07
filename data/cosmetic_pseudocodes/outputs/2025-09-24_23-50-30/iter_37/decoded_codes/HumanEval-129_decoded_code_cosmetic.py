from typing import List


def minPath(alpha: List[List[int]], beta: int) -> List[int]:
    gamma: int = len(alpha)
    delta: int = gamma * gamma + 1
    epsilon: int = 0
    while epsilon < gamma:
        zeta: int = 0
        while zeta < gamma:
            if alpha[epsilon][zeta] == 1:
                eta: List[int] = []
                if epsilon != 0:
                    eta.append(alpha[epsilon - 1][zeta])
                if zeta != 0:
                    eta.append(alpha[epsilon][zeta - 1])
                if epsilon != gamma - 1:
                    eta.append(alpha[epsilon + 1][zeta])
                if zeta != gamma - 1:
                    eta.append(alpha[epsilon][zeta + 1])
                if eta:  # Only update delta if eta has elements
                    delta = min(eta)
            zeta += 1
        epsilon += 1

    theta: List[int] = []
    for i in range(beta):
        tempVal: int = 1 if (i % 2) == 0 else delta
        theta.append(tempVal)

    return theta