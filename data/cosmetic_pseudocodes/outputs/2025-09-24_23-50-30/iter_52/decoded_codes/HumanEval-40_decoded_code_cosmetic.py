from typing import List

def triples_sum_to_zero(alpha: List[int]) -> bool:
    def finder(beta: List[int], gamma: int) -> bool:
        if gamma >= len(beta) - 1:
            return False
        if beta[beta_index] + beta[gamma] + beta[gamma + 1] == 0:
            return True
        return finder(beta, gamma + 1)

    def seeker(delta: int) -> bool:
        nonlocal beta_index
        if delta >= len(alpha) - 2:
            return False
        beta_index = delta
        if finder(alpha, beta_index + 1):
            return True
        return seeker(delta + 1)

    beta_index: int = 0
    return seeker(0)