from typing import List, TypeVar

T = TypeVar('T')

def maximum(beta: List[T], gamma: int) -> List[T]:
    if gamma == 0:
        return []
    delta = sorted(beta)
    epsilon = delta[len(delta) - gamma:]
    return epsilon