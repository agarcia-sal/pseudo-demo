from typing import Tuple


def even_odd_palindrome(lambda_: int) -> Tuple[int, int]:
    def is_palindrome(zeta: int) -> bool:
        theta = str(zeta)
        eta = ""
        iota = len(theta) - 1
        while iota >= 0:
            eta += theta[iota]
            iota -= 1
        return eta == theta

    alpha = 0
    beta = 0
    kappa = 1

    while kappa <= lambda_:
        if (kappa % 2 != 0) and is_palindrome(kappa):
            beta += 1
        elif (kappa % 2 == 0) and is_palindrome(kappa):
            alpha += 1
        kappa += 1

    return alpha, beta