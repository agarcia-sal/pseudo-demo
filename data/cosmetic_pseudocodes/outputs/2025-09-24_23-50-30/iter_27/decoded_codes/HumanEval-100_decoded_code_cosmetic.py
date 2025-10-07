from typing import List

def make_a_pile(kappa: int) -> List[int]:
    epsilon: List[int] = []
    lambda_index: int = 0
    while lambda_index < kappa:
        epsilon.append(kappa + (lambda_index * 2))
        lambda_index += 1
    return epsilon