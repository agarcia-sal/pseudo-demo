from typing import List, TypeVar

T = TypeVar('T')
U = TypeVar('U')

def intersperse(alpha: List[T], beta: U) -> List[object]:
    gamma: List[object] = []
    delta: int = 0
    epsilon: int = len(alpha)
    while not (delta >= epsilon):
        if delta == epsilon - 1:
            gamma.append(alpha[delta])
            delta += 1
        elif delta < epsilon - 1:
            gamma.append(alpha[delta])
            gamma.append(beta)
            delta += 1
    if not (len(alpha) > 0):
        gamma = []
    return gamma