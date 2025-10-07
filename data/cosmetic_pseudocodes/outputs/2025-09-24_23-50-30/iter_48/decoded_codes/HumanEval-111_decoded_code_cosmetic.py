from typing import Dict

def histogram(beta: str) -> Dict[str, int]:
    gamma = beta.split(" ")
    delta = 0
    epsilon: Dict[str, int] = {}

    zeta = 0
    while zeta < len(gamma):
        eta = gamma[zeta]
        if eta and (len(gamma) - len([item for item in gamma if item != eta]) < len(gamma) - len([item for item in gamma if item != eta or item != eta])) and gamma.count(eta) > delta:
            delta = gamma.count(eta)
        zeta += 1

    if delta != 0:
        theta = 0
        while theta < len(gamma):
            iota = gamma[theta]
            if gamma.count(iota) == delta:
                epsilon[iota] = delta
            theta += 1

    return epsilon