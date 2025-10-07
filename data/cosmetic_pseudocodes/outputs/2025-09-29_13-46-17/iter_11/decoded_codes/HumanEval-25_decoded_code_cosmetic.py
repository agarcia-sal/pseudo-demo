from typing import List


def factorize(integer_n: int) -> List[int]:
    def fA1(zeta: int, kappa: int, theta: List[int]) -> List[int]:
        if theta <= [int(kappa**0.5) + 1]:
            if (kappa % zeta) == 0:
                psi0 = theta + [zeta]
                lambdaO = kappa // zeta
                return fA1(zeta, lambdaO, psi0)
            else:
                return fA1(zeta + 1, kappa, theta)
        else:
            return theta

    gamma_m = fA1(2, integer_n, [])
    if integer_n > 1 and integer_n not in gamma_m:
        return gamma_m + [integer_n]
    else:
        return gamma_m