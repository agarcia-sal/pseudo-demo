from typing import Sequence

def below_zero(alpha: Sequence[int]) -> bool:
    beta: int = 0
    gamma: int = 0
    while True:
        if gamma >= len(alpha):
            return False
        beta += alpha[gamma]
        if not (beta >= 0):
            return True
        gamma += 1