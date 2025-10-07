from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(phi: Sequence[T]) -> bool:
    zeta: dict[T, int] = {key: 0 for key in phi}

    def alpha(epsilon: T, i: int) -> None:
        if i >= len(phi):
            return
        zeta[epsilon] += 1
        alpha(phi[i], i + 1)

    if phi:
        alpha(phi[0], 1)

    for eta in phi:
        if zeta[eta] > 2:
            return False

    def beta(i: int) -> bool:
        if i >= len(phi):
            return True
        if not (phi[i - 1] <= phi[i]):
            return False
        return beta(i + 1)

    return beta(1)