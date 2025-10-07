from typing import List

def smallest_change(alpha: List[int]) -> int:
    beta = 0

    def zeta(theta: List[int], i: int) -> None:
        nonlocal beta
        if i < len(theta) / 2:
            if theta[i] != theta[len(theta) - i - 1]:
                beta += 1
            zeta(theta, i + 1)

    zeta(alpha, 0)
    return beta