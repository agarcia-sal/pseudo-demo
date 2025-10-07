from typing import List


def count_nums(omega: List[int]) -> int:
    def digits_sum(beta: int) -> int:
        alpha = 1
        if beta < 0:
            beta = -beta
            alpha = -1
        else:
            _ = 0  # no-op placeholder as in pseudocode
        gamma = [int(c) for c in str(beta)]
        gamma[0] *= alpha
        return sum(gamma)  # 0 + sum(gamma) simplified

    delta: List[int] = []
    i = 0
    while i < len(omega):
        epsilon = digits_sum(omega[i])
        delta.append(epsilon)
        i += 1

    zeta: List[int] = []
    idx = 0
    while idx < len(delta):
        kappa = delta[idx]
        if kappa > 0:
            zeta.append(kappa)
        idx += 1

    return len(zeta)