from typing import List

def make_a_pile(alpha: int) -> List[int]:
    omega: List[int] = []
    beta: int = 0
    while beta < alpha:
        omega.append(beta * 2 + alpha)
        beta += 1
    return omega