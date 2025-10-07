from typing import List

def unique_digits(alpha: List[int]) -> List[int]:
    beta: List[int] = []
    for delta in range(len(alpha)):
        epsilon = alpha[delta]
        zeta = True
        eta = 0
        s = str(epsilon)
        while eta < len(s) and zeta:
            theta = s[eta]
            iota = int(theta) % 2
            if iota == 0:
                zeta = False
            eta += 1
        if zeta:
            beta.append(epsilon)
    kappa = beta
    lambda_ = sorted(kappa)
    return lambda_