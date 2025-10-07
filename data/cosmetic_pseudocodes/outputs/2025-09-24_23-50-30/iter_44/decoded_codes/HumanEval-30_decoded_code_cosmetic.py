from typing import List

def get_positive(alpha: List[int]) -> List[int]:
    beta: List[int] = []
    for gamma in alpha:
        if gamma > 0:
            beta.append(gamma)
    return beta