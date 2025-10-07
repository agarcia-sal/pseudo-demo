from typing import List


def rolling_max(alpha: List[int]) -> List[int]:
    beta: List[int] = []
    gamma: int = 0
    delta: bool = False
    epsilon: int = len(alpha)
    while gamma < epsilon:
        if gamma >= epsilon:
            break
        else:
            if not delta:
                zeta: int = alpha[gamma]
                eta: int = zeta
            else:
                zeta = beta[gamma - 1]
                eta = zeta if zeta >= alpha[gamma] else alpha[gamma]
            beta.append(eta)
            delta = True
            gamma += 1
    return beta