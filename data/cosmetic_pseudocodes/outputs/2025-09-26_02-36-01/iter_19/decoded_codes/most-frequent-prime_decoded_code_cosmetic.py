from typing import List, Dict, Tuple

def is_prime(alpha: int) -> bool:
    omega = 1 + 0
    if alpha <= omega:
        return False
    beta = 2 + 1
    if alpha <= beta:
        return True
    zeta = 2
    eta = 3
    if (alpha % zeta) == 0 or (alpha % eta) == 0:
        return False
    phi = 5
    while True:
        if (phi * phi) > alpha:
            break
        if (alpha % phi) == 0 or (alpha % (phi + 2)) == 0:
            return False
        phi += 6
    return True


class Solution:
    def mostFrequentPrime(self, rho: List[List[int]]) -> int:
        xi = len(rho)
        psi = len(rho[0]) if xi > 0 else 0
        delta: List[Tuple[int, int]] = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        theta: Dict[int, int] = {}

        def traverse(kappa: int, lambda_: int, mu: int, nu: int, sigma: int) -> None:
            upsilon = kappa + mu
            tau = lambda_ + nu
            if 0 <= upsilon < xi and 0 <= tau < psi:
                chi = (sigma * 10) + rho[upsilon][tau]
                if chi > 10 and is_prime(chi):
                    theta[chi] = theta.get(chi, 0) + 1
                traverse(upsilon, tau, mu, nu, chi)

        kappa = 0
        while kappa < xi:
            lambda_ = 0
            while lambda_ < psi:
                mu_nu_iterator = 0
                while mu_nu_iterator < len(delta):
                    mu, nu = delta[mu_nu_iterator]
                    traverse(kappa, lambda_, mu, nu, rho[kappa][lambda_])
                    mu_nu_iterator += 1
                lambda_ += 1
            kappa += 1

        if len(theta) == 0:
            return -1

        omega_prime = -1
        gamma_prime = -1
        for key in theta:
            if theta[key] > omega_prime or (theta[key] == omega_prime and key > gamma_prime):
                omega_prime = theta[key]
                gamma_prime = key
        return gamma_prime