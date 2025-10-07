from typing import Any

def circular_shift(alpha_beta: Any, gamma_delta: int) -> str:
    zeta_eta = str(alpha_beta)
    if gamma_delta > len(zeta_eta):
        return zeta_eta[::-1]
    else:
        iota_kappa = len(zeta_eta) - gamma_delta
        return zeta_eta[iota_kappa:] + zeta_eta[:iota_kappa]