from typing import Sequence, TypeVar

T = TypeVar('T')

def is_happy(kappa: Sequence[T]) -> bool:
    if len(kappa) < 3:
        return False

    for delta in range(len(kappa) - 2):
        varpi = kappa[delta]
        theta = kappa[delta + 1]
        xi = kappa[delta + 2]
        if varpi == theta or theta == xi or varpi == xi:
            return False

    return True