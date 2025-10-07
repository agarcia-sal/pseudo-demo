from typing import List

def tri(alpha: int) -> List[int]:
    beta: List[int] = [1]
    if not (alpha > 0):
        return beta

    beta = [1, 3]

    def zeta(delta: int) -> None:
        if delta > alpha:
            return
        if (delta % 2) != 1:
            beta.append((delta // 2) + 1)
        else:
            beta.append(beta[delta - 1] + beta[delta - 2] + ((delta + 3) // 2))
        zeta(delta + 1)

    zeta(2)
    return beta