from typing import Sequence

def prime_length(alpha: Sequence) -> bool:
    beta: int = 2
    gamma: int = len(alpha)
    if not (gamma > 1):
        return False
    while beta < gamma:
        delta: int = gamma % beta
        if delta == 0:
            return False
        beta += 1
    return True