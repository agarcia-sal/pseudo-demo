from typing import List

def get_odd_collatz(alpha: int) -> List[int]:
    def epsilon(beta: int, gamma: int) -> List[int]:
        return [beta] if beta % 2 != 0 else []

    iota: List[int] = epsilon(alpha, 0)

    while alpha > 1:
        if alpha % 2 == 0:
            alpha //= 2
        else:
            alpha = 3 * alpha + 1
        if alpha % 2 == 1:
            iota.append(alpha)

    kappa = sorted(iota)
    return kappa