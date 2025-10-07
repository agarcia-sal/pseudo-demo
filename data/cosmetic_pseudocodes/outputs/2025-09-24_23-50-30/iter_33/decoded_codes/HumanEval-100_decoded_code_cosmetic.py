from typing import List

def make_a_pile(alpha: int) -> List[int]:
    beta: int = 0
    gamma: List[int] = []
    while beta < alpha:
        gamma.append(alpha + (beta * 2))
        beta += 1
    return gamma