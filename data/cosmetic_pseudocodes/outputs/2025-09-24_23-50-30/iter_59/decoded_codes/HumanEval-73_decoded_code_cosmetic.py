from typing import Sequence

def smallest_change(beta: Sequence[bool]) -> int:
    gamma: int = 0
    delta: int = 0
    epsilon: int = len(beta)
    while delta < epsilon / 2:
        if beta[delta] != beta[(epsilon - delta) - 1]:
            gamma += 1
        delta += 1
    return gamma