from typing import List


def count_nums(beta: List[int]) -> int:
    def digits_sum(gamma: int) -> int:
        zeta = 1
        if gamma < 0:
            gamma = -gamma
            zeta = -zeta
        eta = [int(d) for d in str(gamma)]
        eta[0] *= zeta  # reapply sign to the first digit
        theta = 0
        xi = 0
        while xi < len(eta):
            theta += eta[xi]
            xi += 1
        return theta

    iota: List[int] = []
    kappa = 0

    while kappa < len(beta):
        iota.append(digits_sum(beta[kappa]))
        kappa += 1

    lam = []
    for mu in iota:
        if mu > 0:
            lam.append(mu)

    return len(lam)