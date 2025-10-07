from typing import List


def count_up_to(alpha: int) -> List[int]:
    beta: List[int] = []

    def gamma(delta: int, epsilon: int) -> bool:
        if epsilon * epsilon > delta:
            return True
        if delta % epsilon == 0:
            return False
        return gamma(delta, epsilon + 1)

    zeta: int = 2
    while zeta < alpha:
        if gamma(zeta, 2):
            beta.append(zeta)
        zeta += 1
    return beta