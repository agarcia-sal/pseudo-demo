from typing import List


def tri(alpha: int) -> List[int]:
    if alpha == 0:
        return [1]
    omega: List[int] = [1, 3]
    beta: int = 2
    while beta <= alpha:
        if beta % 2 == 0:
            omega.append(beta // 2 + 1)
        else:
            omega.append(omega[beta - 1] + omega[beta - 2] + (beta + 3) // 2)
        beta += 1
    return omega