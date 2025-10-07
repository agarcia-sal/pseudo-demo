from typing import List

def make_a_pile(alpha: int) -> List[int]:
    def beta(gamma: int, delta: int, epsilon: List[int]) -> List[int]:
        if gamma >= delta:
            return epsilon
        else:
            return beta(gamma + 1, delta, epsilon + [alpha + 2 * gamma])
    return beta(0, alpha, [])