from typing import List


def words_string(beta: str) -> List[str]:
    delta: List[str] = []
    if beta:
        gamma: int = 0
        while gamma < len(beta):
            epsilon: str = beta[gamma]
            if epsilon == ',':
                delta.append(' ')
            else:
                delta.append(epsilon)
            gamma += 1

        zeta: str = ''
        eta: int = 0
        while eta < len(delta):
            zeta += delta[eta]
            eta += 1

        theta: List[str] = zeta.split()
        return theta
    else:
        return []