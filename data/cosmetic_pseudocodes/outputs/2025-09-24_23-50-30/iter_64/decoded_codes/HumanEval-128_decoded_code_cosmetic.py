from typing import List, Optional


def prod_signs(beta: List[int]) -> Optional[int]:
    if len(beta) == 0:
        return None

    epsilon: int = 1
    for idx in range(len(beta)):
        if beta[idx] == 0:
            epsilon = 0
            break

    if epsilon != 0:
        zeta: int = 0
        alpha: int = 0
        while alpha < len(beta):
            if beta[alpha] < 0:
                zeta += 1
            alpha += 1

        epsilon = 1
        alpha = 0
        while alpha < zeta:
            epsilon *= -1
            alpha += 1

    theta: int = 0
    vari: int = 0
    while vari < len(beta):
        theta += abs(beta[vari])
        vari += 1

    return epsilon * theta