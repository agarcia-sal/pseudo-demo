from typing import List

def make_a_pile(alpha: int) -> List[int]:
    beta: List[int] = []
    gamma: int = 0
    while gamma < alpha:
        beta.append(alpha + (2 * gamma))
        gamma += 1
    return beta