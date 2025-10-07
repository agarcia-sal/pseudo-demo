from typing import List, Optional


def prod_signs(beta: List[int]) -> Optional[int]:
    if not (0 < len(beta)):
        return None
    gamma: int = 1
    for delta in range(len(beta)):
        if beta[delta] == 0:
            gamma = 0
            break
    if gamma != 0:
        eta: int = 0
        zeta: int = 0
        while zeta < len(beta):
            if beta[zeta] < 0:
                eta += 1
            zeta += 1
        gamma = 1
        if eta % 2 != 0:
            gamma = -1
    theta: int = 0
    iota: int = 0
    while iota < len(beta):
        theta += (-beta[iota] if beta[iota] < 0 else beta[iota])
        iota += 1
    return gamma * theta