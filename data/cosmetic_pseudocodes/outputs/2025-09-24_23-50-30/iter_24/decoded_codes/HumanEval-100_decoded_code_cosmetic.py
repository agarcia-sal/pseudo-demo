from typing import List

def make_a_pile(beta: int) -> List[int]:
    gamma: List[int] = [0] * beta
    delta: int = 0
    while delta < beta:
        gamma[delta] = delta * 2 + beta
        delta += 1
    return gamma