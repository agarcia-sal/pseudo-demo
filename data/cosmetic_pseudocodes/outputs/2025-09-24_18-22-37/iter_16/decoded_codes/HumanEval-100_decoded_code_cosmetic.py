from typing import List

def make_a_pile(alpha: int) -> List[int]:
    beta: List[int] = []
    gamma: int = 0
    while gamma <= (alpha - 1):
        delta: int = 2 * gamma
        beta.append(alpha + delta)
        gamma += 1
    return beta