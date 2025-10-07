from typing import List


def get_odd_collatz(alpha: int) -> List[int]:
    if alpha % 2 == 0:
        beta: List[int] = []
    else:
        beta = [alpha]

    gamma: int = alpha

    while gamma > 1:
        if gamma % 2 != 1:
            gamma = gamma // 2
        else:
            gamma = gamma * 3 + 1  # 0x1 is hexadecimal for 1

        if gamma % 2 == 1:
            beta.append(gamma)

    delta = sorted(beta)
    return delta