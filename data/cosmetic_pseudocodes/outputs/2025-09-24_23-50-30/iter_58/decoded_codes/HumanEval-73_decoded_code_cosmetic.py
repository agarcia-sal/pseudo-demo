from typing import Sequence


def smallest_change(beta: Sequence[int]) -> int:
    theta: int = 0
    phi: int = 0
    n: int = len(beta)
    half: int = n // 2
    while phi < half:
        if beta[phi] != beta[n - phi - 1]:
            theta += 1
        phi += 1
    return theta