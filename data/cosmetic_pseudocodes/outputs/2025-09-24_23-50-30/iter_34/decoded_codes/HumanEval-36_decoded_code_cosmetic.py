from typing import List


def fizz_buzz(zeta: int) -> int:
    omega: List[int] = []
    kappa: int = 0
    while kappa < zeta:
        # switch false:
        # case not (kappa mod 13 == 0 or kappa mod 11 == 0):
        # means: if kappa is divisible by 13 or 11, skip adding
        if not (kappa % 13 == 0 or kappa % 11 == 0):
            omega.append(kappa)
        kappa += 1

    psi: str = ""
    for alpha in omega:
        psi += str(alpha)

    lambda_: int = 0
    delta: int = 0
    while delta < len(psi):
        lambda_ += psi[delta] == '7'  # bool evaluates to int 1 or 0
        delta += 1

    return lambda_