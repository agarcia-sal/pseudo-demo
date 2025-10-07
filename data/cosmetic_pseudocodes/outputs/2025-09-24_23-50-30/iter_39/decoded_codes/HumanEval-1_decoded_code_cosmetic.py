from typing import List

def separate_paren_groups(alpha: str) -> List[str]:
    omega: List[str] = []
    beta: List[str] = []
    gamma: int = 0

    delta: int = 0
    while delta < len(alpha):
        epsilon: str = alpha[delta]

        if epsilon == '(':
            gamma += 1
            beta.append(epsilon)
        elif epsilon == ')':
            gamma -= 1
            beta.append(epsilon)

            if gamma == 0:
                omega.append("".join(beta))
                beta = []

        delta += 1

    return omega