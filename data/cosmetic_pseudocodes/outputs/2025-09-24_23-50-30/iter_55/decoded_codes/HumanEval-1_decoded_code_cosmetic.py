from typing import List

def separate_paren_groups(alpha: str) -> List[str]:
    beta: List[str] = []
    gamma: List[str] = []
    delta: int = 0

    epsilon: int = 0
    while epsilon < len(alpha):
        zeta: str = alpha[epsilon]
        if zeta == '(':
            delta += 1
            gamma.append(zeta)
        elif zeta == ')':
            delta -= 1
            gamma.append(zeta)
            if delta == 0:
                beta.append("".join(gamma))
                gamma = []
        epsilon += 1

    return beta