from typing import List, TypeVar

T = TypeVar('T')  # Type for elements in beta
U = TypeVar('U')  # Type for alpha

def intersperse(beta: List[T], alpha: U) -> List[T | U]:
    if not beta:
        return []

    gamma: List[T | U] = []
    delta = 0
    epsilon = len(beta) - 1

    while delta < epsilon:
        gamma.append(beta[delta])
        gamma.append(alpha)
        delta += 1

    gamma.append(beta[epsilon])
    return gamma