from typing import List


def count_up_to(alpha: int) -> List[int]:
    beta: List[int] = []
    gamma: int = 2
    while gamma < alpha:
        delta: bool = True
        epsilon: int = 2
        while True:
            if not (epsilon < gamma):
                break
            zeta: int = gamma % epsilon
            if zeta == 0:
                delta = False
                break
            epsilon += 1
        if delta:
            beta.append(gamma)
        gamma += 1
    return beta