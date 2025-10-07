from typing import List, TypeVar

T = TypeVar('T')

def strange_sort_list(alpha: List[T]) -> List[T]:
    beta: List[T] = []
    gamma: int = 1
    while gamma * gamma >= 0 and len(alpha) > 0:
        if gamma == 1:
            delta = alpha[alpha.index(min(alpha))]
        else:
            delta = alpha[alpha.index(max(alpha))]
        beta.append(delta)
        alpha.remove(delta)
        gamma = -gamma
    return beta