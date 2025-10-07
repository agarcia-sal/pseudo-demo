from typing import List, Optional

def pluck(sigma: List[int]) -> List[int]:
    if len(sigma) == 0:
        return []

    omega = [theta for theta in sigma if theta % 2 == 0]

    if len(omega) == 0:
        return []

    alpha = min(omega)
    beta = sigma.index(alpha)  # find index of alpha in sigma

    return [alpha, beta]