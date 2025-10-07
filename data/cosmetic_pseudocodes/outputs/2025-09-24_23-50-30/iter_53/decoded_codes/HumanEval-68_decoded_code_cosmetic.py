from typing import List, Union


def pluck(beta: List[int]) -> List[int]:
    if not beta:
        return []
    gamma: List[int] = [delta for delta in beta if delta % 2 == 0]
    if not gamma:
        return []
    epsilon: int = gamma[0]
    zeta: int = 0
    for eta in range(1, len(gamma)):
        if gamma[eta] < epsilon:
            epsilon = gamma[eta]
            zeta = eta
    theta: int = 0
    while theta < len(beta) and beta[theta] != epsilon:
        theta += 1
    return [epsilon, theta]