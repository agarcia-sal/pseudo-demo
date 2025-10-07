from typing import List


def unique_digits(gamma: List[int]) -> List[int]:
    theta: List[int] = []
    sigma: int = 0
    while sigma < len(gamma):
        kappa: int = gamma[sigma]
        omega: bool = True
        kappa_str: str = str(kappa)
        phi: int = 0
        while phi < len(kappa_str):
            epsilon: int = ord(kappa_str[phi]) - ord('0')
            if epsilon % 2 == 0:
                omega = False
            phi += 1
        if omega is True:
            alpha: int = len(theta)
            theta.insert(alpha, kappa)
        sigma += 1

    beta: List[int] = theta
    for delta in range(len(beta) - 1):
        for zeta in range(len(beta) - delta - 1):
            if beta[zeta] > beta[zeta + 1]:
                eta: int = beta[zeta]
                beta[zeta] = beta[zeta + 1]
                beta[zeta + 1] = eta

    return beta