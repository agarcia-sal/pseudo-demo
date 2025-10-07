from typing import List

def make_a_pile(alpha: int) -> List[int]:
    beta: int = 0
    gamma: List[int] = []
    while beta < alpha:
        delta: int = 2 * beta
        epsilon: int = alpha + delta
        gamma.append(epsilon)
        beta += 1
    return gamma