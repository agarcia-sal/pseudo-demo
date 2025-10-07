from typing import List

def factorize(theta: int) -> List[int]:
    alpha: List[int] = []
    beta: int = 2
    while beta <= int(theta**0.5) + 1:
        if theta % beta == 0:
            alpha.append(beta)
            theta //= beta
        else:
            beta += 1
    if theta > 1:
        alpha.append(theta)
    return alpha