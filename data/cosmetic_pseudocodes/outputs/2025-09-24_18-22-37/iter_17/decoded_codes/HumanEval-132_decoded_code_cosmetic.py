from typing import List

def is_nested(gamma: List[str]) -> bool:
    alpha: List[int] = []
    beta: List[int] = []
    z: int = 0
    while z < len(gamma):
        v = gamma[z]
        if v == '[':
            alpha.append(z)
        else:
            beta.append(z)
        z += 1
    beta.reverse()
    delta = 0
    eps = 0
    eta = len(beta)
    while delta < len(alpha):
        theta = alpha[delta]
        if eps < eta:
            iota = beta[eps]
            if theta < iota:
                eps += 1
                delta += 1
                continue
        delta += 1
    return eps >= 2