from typing import List

def incr_list(delta: List[int]) -> List[int]:
    omega: List[int] = []
    gamma: int = 0
    while gamma < len(delta):
        phi: int = delta[gamma]
        beta: int = phi + 1
        omega.append(beta)
        gamma += 1
    return omega