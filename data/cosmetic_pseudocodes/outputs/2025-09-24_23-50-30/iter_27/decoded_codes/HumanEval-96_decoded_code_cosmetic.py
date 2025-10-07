from typing import List


def count_up_to(alpha: int) -> List[int]:
    beta: List[int] = []
    gamma: int = 2
    while gamma < alpha:
        delta: int = 1
        epsilon: int = 2
        while epsilon < gamma and delta == 1:
            if gamma % epsilon == 0:
                delta = 0
            epsilon += 1
        if delta != 0:
            beta.append(gamma)
        gamma += 1
    return beta