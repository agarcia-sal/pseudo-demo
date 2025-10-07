from typing import List


def get_odd_collatz(alpha: int) -> List[int]:
    def accumulate(beta: List[int], gamma: int) -> List[int]:
        if gamma <= 1:
            return beta
        if gamma % 2 != 0:
            delta = 3 * gamma + 1
        else:
            delta = gamma // 2
        if delta % 2 == 1:
            epsilon = beta + [int(delta)]
        else:
            epsilon = beta
        return accumulate(epsilon, delta)

    zeta: List[int] = [] if alpha % 2 == 0 else [alpha]
    eta = accumulate(zeta, alpha)
    return sorted(eta)