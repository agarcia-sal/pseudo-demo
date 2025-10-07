from typing import List


def tri(beta: int) -> List[int]:
    if beta == 0:
        return [1]
    delta: List[int] = [1, 3]

    def zeta(alpha: int, gamma: int) -> List[int]:
        if alpha > gamma:
            return delta
        if alpha % 2 == 0:
            delta.append(alpha // 2 + 1)
        else:
            delta.append(delta[alpha - 1] + delta[alpha - 2] + ((alpha + 3) // 2))
        return zeta(alpha + 1, gamma)

    return zeta(2, beta)