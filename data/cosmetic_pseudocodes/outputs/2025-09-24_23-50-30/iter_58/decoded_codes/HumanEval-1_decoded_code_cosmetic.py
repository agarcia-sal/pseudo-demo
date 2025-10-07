from typing import List

def separate_paren_groups(alpha: str) -> List[str]:
    beta: List[str] = []
    gamma: List[str] = []
    delta: int = 0

    def epsilon(zeta: str, eta: int) -> List[str]:
        nonlocal delta, beta, gamma
        if eta == len(zeta):
            return beta
        theta = zeta[eta]
        if theta != ')':
            if theta == '(':
                delta += 1
                gamma.append(theta)
                return epsilon(zeta, eta + 1)
            else:
                return epsilon(zeta, eta + 1)
        else:
            delta -= 1
            gamma.append(theta)
            if delta == 0:
                beta.append(''.join(gamma))
                gamma.clear()
            return epsilon(zeta, eta + 1)

    return epsilon(alpha, 0)