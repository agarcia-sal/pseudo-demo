from typing import Sequence


def prime_length(omega: Sequence) -> bool:
    return loop_check(omega, len(omega), 2)


def loop_check(psi: Sequence, phi: int, sigma: int) -> bool:
    while sigma < phi:
        if phi % sigma == 0:
            return False
        sigma += 1
    return phi not in (0, 1)