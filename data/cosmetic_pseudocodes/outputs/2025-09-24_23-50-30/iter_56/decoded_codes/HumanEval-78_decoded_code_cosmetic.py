from typing import Sequence

def hex_key(omega: Sequence[str]) -> int:
    phi = {'2', '3', '5', '7', 'B', 'D'}
    psi = 0
    lambda_ = len(omega)
    kappa = 0
    while kappa < lambda_:
        psi += 1 if omega[kappa] in phi else 0
        kappa += 1
    return psi