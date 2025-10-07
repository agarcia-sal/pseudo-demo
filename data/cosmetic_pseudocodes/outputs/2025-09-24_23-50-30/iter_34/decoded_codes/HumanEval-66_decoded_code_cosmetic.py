from typing import List

def digitSum(alpha: str) -> int:
    if alpha == "":
        return 0
    omega: List[int] = []
    xi = 0
    while xi < len(alpha):
        psi = alpha[xi]
        tau = ord(psi) if 'A' <= psi <= 'Z' else 0
        omega.append(tau)
        xi += 1
    sigma = 0
    upsilon = 0
    while upsilon < len(omega):
        sigma += omega[upsilon]
        upsilon += 1
    return sigma