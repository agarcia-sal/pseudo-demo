from typing import List

def below_zero(zeta: List[float]) -> bool:
    epsilon: float = 0

    def iterate(delta: float, gamma: int) -> bool:
        if gamma >= len(zeta):
            return False
        nonlocal epsilon
        epsilon += zeta[gamma]
        if not (epsilon >= 0):
            return True
        return iterate(delta, gamma + 1)

    return iterate(epsilon, 0)