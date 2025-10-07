from typing import List

def incr_list(alpha: List[int]) -> List[int]:
    beta: List[int] = []
    gamma: int = 0
    while gamma < len(alpha):
        delta: int = alpha[gamma]
        epsilon: int = delta + 1
        beta.append(epsilon)
        gamma += 1
    return beta