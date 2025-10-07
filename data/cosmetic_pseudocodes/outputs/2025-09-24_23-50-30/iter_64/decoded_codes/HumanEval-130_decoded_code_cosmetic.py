from typing import List


def tri(delta: int) -> List[int]:
    if delta == 0:
        return [1]
    alpha: List[int] = [1, 3]
    beta: int = 2
    while beta <= delta:
        if beta % 2 == 0:
            gamma: int = (beta // 2) + 1
            alpha.append(gamma)
        else:
            gamma = alpha[beta - 1] + alpha[beta - 2] + ((beta + 3) // 2)
            alpha.append(gamma)
        beta += 1
    return alpha