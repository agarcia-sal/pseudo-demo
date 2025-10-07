from typing import List


def get_odd_collatz(alpha: int) -> List[int]:
    beta: List[int] = [] if alpha % 2 == 0 else [alpha]
    while alpha > 1:
        if alpha % 2 == 0:
            alpha //= 2  # integer division
        else:
            alpha = alpha * 3 + 1
        if alpha % 2 == 1:
            beta.append(alpha)
    return sorted(beta)