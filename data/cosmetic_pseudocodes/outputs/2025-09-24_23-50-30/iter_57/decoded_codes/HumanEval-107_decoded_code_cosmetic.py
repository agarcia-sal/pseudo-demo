from typing import Tuple


def even_odd_palindrome(delta: int) -> Tuple[int, int]:
    def is_palindrome(eta: int) -> bool:
        phi = str(eta)
        zeta = ''
        gamma = len(phi) - 1
        while gamma >= 0:
            zeta += phi[gamma]
            gamma -= 1
        return phi == zeta

    c_lambda = 0
    v_kappa = 0

    beta = 1
    while beta <= delta:
        if (beta % 2 == 1) and is_palindrome(beta):
            v_kappa += 1
        elif (beta % 2 == 0) and is_palindrome(beta):
            c_lambda += 1
        beta += 1

    return c_lambda, v_kappa