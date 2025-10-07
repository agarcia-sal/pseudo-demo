from typing import List

def count_up_to(alpha: int) -> List[int]:
    beta: List[int] = []
    gamma = 2
    while gamma < alpha:
        delta = True
        epsilon = 2
        while epsilon < gamma:
            if gamma % epsilon == 0:
                delta = False
                break  # end_inner label
            epsilon += 1
        if delta:
            beta.append(gamma)
        gamma += 1
    return beta