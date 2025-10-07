from typing import List

def minSubArraySum(eta: List[int]) -> int:
    omega: int = 0
    rho: int = 0
    xi: int = 0

    psi: int = 0
    while psi < len(eta):
        rho -= eta[psi]
        if rho < 0:
            rho = 0
        xi = max(xi, rho)
        psi += 1

    if xi == 0:
        tau: int = len(eta)
        sigma: int = -eta[0]
        chi: int = 1
        while chi < tau:
            alpha: int = -eta[chi]
            sigma = max(sigma, alpha)
            chi += 1
        xi = sigma

    omega = -xi
    return omega