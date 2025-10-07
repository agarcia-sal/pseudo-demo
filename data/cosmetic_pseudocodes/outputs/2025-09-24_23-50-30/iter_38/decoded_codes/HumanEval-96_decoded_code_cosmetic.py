from typing import List


def count_up_to(x: int) -> List[int]:
    beta: List[int] = []
    alpha: int = 2
    while alpha < x:
        delta: bool = True
        gamma: int = 2
        while gamma < alpha:
            if alpha % gamma == 0:
                delta = False
                break
            gamma += 1
        if delta:
            beta.append(alpha)
        alpha += 1
    return beta