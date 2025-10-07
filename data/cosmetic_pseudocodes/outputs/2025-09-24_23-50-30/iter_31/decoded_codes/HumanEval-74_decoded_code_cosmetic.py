from typing import Sequence, Union

def total_match(alpha: Sequence[str], beta: Sequence[str]) -> Sequence[str]:
    xi: int = 0
    gamma: int = 0
    while gamma < len(alpha):
        xi += len(alpha[gamma])
        gamma += 1
    psi: int = 0
    kappa: int = 0
    while kappa < len(beta):
        psi += len(beta[kappa])
        kappa += 1
    return alpha if xi <= psi else beta