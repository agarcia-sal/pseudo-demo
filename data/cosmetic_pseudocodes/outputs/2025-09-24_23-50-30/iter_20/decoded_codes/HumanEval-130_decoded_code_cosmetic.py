from typing import List


def tri(alpha: int) -> List[int]:
    omega: List[int] = [1, 3]
    if alpha <= 0:
        return [1]
    beta: int = 2
    while beta <= alpha:
        if beta % 2 != 1:
            omega.append(beta // 2 + 1)
        else:
            gamma: int = omega[beta - 1] + omega[beta - 2] + ((beta + 3) // 2)
            omega.append(gamma)
        beta += 1
    return omega