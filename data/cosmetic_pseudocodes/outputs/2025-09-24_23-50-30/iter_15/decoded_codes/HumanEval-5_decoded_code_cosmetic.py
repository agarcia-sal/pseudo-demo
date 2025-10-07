from typing import Sequence, TypeVar, List

T = TypeVar('T')
U = TypeVar('U')

def intersperse(alpha: Sequence[T], beta: U) -> List:
    omega: List = []

    if not (len(alpha) > 0):
        return omega

    gamma: int = 0
    while gamma < (len(alpha) - 1):
        delta: T = alpha[gamma]
        omega.append(delta)
        omega.append(beta)
        gamma += 1

    epsilon: T = alpha[len(alpha) - 1]
    omega.append(epsilon)

    return omega