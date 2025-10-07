from typing import List, TypeVar

T = TypeVar('T')

def unique(alpha: List[T]) -> List[T]:
    beta: List[T] = []
    for gamma in alpha:
        found = False
        for delta in beta:
            if delta == gamma:
                found = True
                break
        if not found:
            beta.append(gamma)
    for epsilon in range(len(beta) - 1):
        for zeta in range(epsilon + 1, len(beta)):
            if beta[epsilon] > beta[zeta]:
                beta[epsilon], beta[zeta] = beta[zeta], beta[epsilon]
    return beta