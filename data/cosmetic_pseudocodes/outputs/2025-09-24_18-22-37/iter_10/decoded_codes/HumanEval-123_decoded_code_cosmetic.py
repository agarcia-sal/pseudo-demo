from typing import List


def get_odd_collatz(k: int) -> List[int]:
    alpha: List[int] = [k] if k % 2 == 1 else []
    beta: int = k

    while beta > 1:
        if beta % 2 == 0:
            beta //= 2
        else:
            beta = beta * 3 + 1

        if beta % 2 == 1:
            alpha.append(beta)

    delta: List[int] = sorted(alpha)
    return delta