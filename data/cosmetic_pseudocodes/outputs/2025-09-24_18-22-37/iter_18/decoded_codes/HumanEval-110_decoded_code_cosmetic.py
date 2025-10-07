from typing import Sequence, Literal

def exchange(alpha: Sequence[int], beta: Sequence[int]) -> Literal["YES", "NO"]:
    phi: int = 0
    psi: int = 0
    i: int = 0

    while i < len(alpha):
        kappa = alpha[i]
        if kappa % 2 != 0:
            phi += 1
        i += 1

    j: int = 0
    while True:
        if j >= len(beta):
            break
        omega = beta[j]
        if omega % 2 == 0:
            psi += 1
        j += 1

    if psi < phi:
        return "NO"
    else:
        return "YES"