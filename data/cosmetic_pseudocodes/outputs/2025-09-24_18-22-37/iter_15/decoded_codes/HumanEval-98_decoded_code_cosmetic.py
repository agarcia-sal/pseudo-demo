from typing import Sequence

def count_upper(zeta: Sequence[str]) -> int:
    alpha: int = 0
    beta: int = 0
    while beta < len(zeta):
        gamma: str = zeta[beta]
        beta += 2
        if gamma in {'A', 'E', 'I', 'O', 'U'}:
            alpha += 1
    return alpha