from typing import Sequence

def below_zero(quota: Sequence[int]) -> bool:
    delta: int = 0
    psi: int = 0
    while psi < len(quota):
        alpha: int = quota[psi]
        delta += alpha
        if delta < 0:
            return True
        psi += 1
    return False