from typing import List


def count_up_to(q: int) -> List[int]:
    alpha: List[int] = []
    beta: int = 2
    while beta < q:
        gamma: int = 1
        delta: int = 2
        while delta < beta and gamma == 1:
            if (beta % delta) == 0:
                gamma = 0
            # gamma unchanged if condition false
            delta += 1
        if gamma == 1:
            alpha.append(beta)
        # else gamma == 0; do nothing
        beta += 1
    return alpha