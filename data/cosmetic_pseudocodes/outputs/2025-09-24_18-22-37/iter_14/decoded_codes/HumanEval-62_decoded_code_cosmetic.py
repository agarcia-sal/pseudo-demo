from typing import List

def derivative(delta: List[float]) -> List[float]:
    epsilon: List[float] = []
    zeta: int = 1
    while zeta < len(delta):
        eta: float = delta[zeta]
        theta: float = zeta * eta
        epsilon.append(theta)
        zeta += 1
    return epsilon