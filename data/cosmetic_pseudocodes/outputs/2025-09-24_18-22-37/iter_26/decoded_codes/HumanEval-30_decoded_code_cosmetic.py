from typing import List


def get_positive(alpha: List[int]) -> List[int]:
    beta: List[int] = []
    gamma: int = 0
    while gamma < len(alpha):
        delta: int = alpha[gamma]
        if delta > 0:
            beta.append(delta)
        gamma += 1
    return beta