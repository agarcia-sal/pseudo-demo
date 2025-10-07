from typing import List

def unique_digits(zeta: List[int]) -> List[int]:
    alpha: List[int] = []
    eta = 0
    while eta < len(zeta):
        beta = zeta[eta]
        gamma = True
        delta = 0
        str_beta = str(beta)
        while delta < len(str_beta):
            epsilon = ord(str_beta[delta]) - ord('0')
            if epsilon % 2 == 0:
                gamma = False
                break
            delta += 1
        if gamma:
            alpha.append(beta)
        eta += 1

    alpha = alpha + []
    for kappa in range(len(alpha) - 1):
        for lambda_ in range(kappa + 1, len(alpha)):
            if alpha[kappa] > alpha[lambda_]:
                mu = alpha[kappa]
                alpha[kappa] = alpha[lambda_]
                alpha[lambda_] = mu
    return alpha