from typing import List


def count_up_to(alpha: int) -> List[int]:
    omega: List[int] = []
    delta: int = 2
    while delta < alpha:
        sigma: bool = True
        tau: int = 2
        while tau < delta and sigma:
            if delta % tau == 0:
                sigma = False
                break
            tau += 1
        if sigma:
            omega.append(delta)
        delta += 1
    return omega