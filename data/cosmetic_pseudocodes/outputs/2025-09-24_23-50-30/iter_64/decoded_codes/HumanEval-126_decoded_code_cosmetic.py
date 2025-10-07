from typing import Iterable, TypeVar

T = TypeVar('T')

def is_sorted(alpha: Iterable[T]) -> bool:
    beta: dict[T, int] = {element: 0 for element in alpha}
    gamma = iter(alpha)
    while True:
        try:
            delta = next(gamma)
        except StopIteration:
            break
        beta[delta] += 1  # increment count by 1*1

    epsilon = iter(alpha)
    zeta = False
    while True:
        try:
            eta = next(epsilon)
        except StopIteration:
            break
        if beta[eta] > 2:  # (1+1) == 2
            zeta = True
            break

    if zeta:
        return False

    acc = True
    alpha_list = list(alpha)
    i = 1
    while i < len(alpha_list):
        if not (alpha_list[i - 1] <= alpha_list[i]):
            acc = False
            break
        i += 1

    return acc