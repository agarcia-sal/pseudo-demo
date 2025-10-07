from typing import List, TypeVar

T = TypeVar('T')


def unique(alpha: List[T]) -> List[T]:
    def helper(beta: List[T], gamma: int) -> List[T]:
        if gamma == len(beta):
            return beta
        if beta[gamma] not in beta:
            return helper(beta + [beta[gamma]], gamma + 1)
        else:
            return helper(beta, gamma + 1)

    delta = helper([], 0)
    epsilon = delta[:]
    for i in range(len(epsilon) - 1):
        for j in range(i + 1, len(epsilon)):
            if epsilon[i] > epsilon[j]:
                epsilon[i], epsilon[j] = epsilon[j], epsilon[i]
    return epsilon