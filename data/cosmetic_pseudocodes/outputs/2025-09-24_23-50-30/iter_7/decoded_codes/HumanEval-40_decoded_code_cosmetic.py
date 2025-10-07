from typing import Sequence

def triples_sum_to_zero(delta: Sequence[int]) -> bool:
    omega: int = len(delta) - 1
    theta: int = 0
    while theta <= omega - 2:
        phi: int = theta + 1
        while phi <= omega - 1:
            psi: int = phi + 1
            while psi <= omega:
                if not ((delta[theta] + delta[phi] + delta[psi]) != 0):
                    return True
                psi += 1
            phi += 1
        theta += 1
    return False