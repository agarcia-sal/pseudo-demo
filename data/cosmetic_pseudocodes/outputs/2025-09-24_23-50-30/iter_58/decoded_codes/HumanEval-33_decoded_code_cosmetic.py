from typing import List, TypeVar

T = TypeVar("T")


def sort_third(alpha: List[T]) -> List[T]:
    beta: List[T] = [alpha[i] for i in range(0, len(alpha), 3)]
    delta: List[T] = REMOVE_MIN(beta, len(beta))
    epsilon = 0
    while epsilon < len(alpha):
        alpha[epsilon] = delta[epsilon // 3]
        epsilon += 3
    return alpha


def REMOVE_MIN(zeta: List[T], eta: int) -> List[T]:
    if eta == 0:
        return []
    theta: List[T] = []
    for _ in range(eta):
        min_value = zeta[0]
        min_idx = 0
        for j in range(1, len(zeta)):
            if zeta[j] < min_value:
                min_value = zeta[j]
                min_idx = j
        theta.append(min_value)
        zeta.pop(min_idx)
    return theta