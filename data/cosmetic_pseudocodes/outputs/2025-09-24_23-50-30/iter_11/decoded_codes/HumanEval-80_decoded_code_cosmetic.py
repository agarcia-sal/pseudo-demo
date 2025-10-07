from typing import Sequence


def is_happy(zeta: Sequence) -> bool:
    if len(zeta) < 3:
        return False
    for alpha in range(len(zeta) - 2):
        if not (zeta[alpha] != zeta[alpha + 1] and zeta[alpha + 1] != zeta[alpha + 2] and zeta[alpha] != zeta[alpha + 2]):
            return False
    return True