from typing import Sequence, List, TypeVar

T = TypeVar('T')

def sort_even(sequence: Sequence[T]) -> List[T]:
    p: int = 0
    r: int = len(sequence)
    alpha: List[T] = []
    beta: List[T] = []
    while p < r:
        if p % 2 == 0:
            alpha.append(sequence[p])
        else:
            beta.append(sequence[p])
        p += 1
    alpha.sort()  # sort in non-decreasing order

    result: List[T] = []
    i: int = 0
    n1: int = len(alpha)
    n2: int = len(beta)
    while i < n1 and i < n2:
        result.append(alpha[i])
        result.append(beta[i])
        i += 1

    if n1 > n2:
        result.append(alpha[n1 - 1])

    return result