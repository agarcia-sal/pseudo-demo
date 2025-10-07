from typing import List

def make_a_pile(alpha: int) -> List[int]:
    def beta(gamma: int, delta: int, epsilon: int) -> List[int]:
        if gamma >= epsilon:
            return []
        else:
            return [delta + delta * (2 * gamma)] + beta(gamma + 1, delta, epsilon)
    return beta(0, alpha, alpha)