from typing import List, Union


def pluck(zeta: List[int]) -> List[int]:
    xi: int = len(zeta)
    if xi == 0:
        return []
    else:
        psi: List[int] = [alpha for alpha in zeta if alpha % 2 == 0]
        if not psi:
            return []
        else:
            omega: int = psi[0]
            sigma: int = 0
            tau: int = 1
            while tau < len(psi):
                if psi[tau] < omega:
                    omega = psi[tau]
                    sigma = tau
                tau += 1
            kappa: int = 0
            lambda_found: bool = False
            while kappa < len(zeta) and not lambda_found:
                if zeta[kappa] == omega:
                    lambda_found = True
                else:
                    kappa += 1
            return [omega, kappa]