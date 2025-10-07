from typing import List

def filter_by_prefix(lambda_omega: List[str], gamma_eta: str) -> List[str]:
    kappa_phi: List[str] = []
    mu_sigma: int = 0
    while mu_sigma < len(lambda_omega):
        # If gamma_eta is not longer than lambda_omega[mu_sigma] and the prefix matches
        if not (len(gamma_eta) > len(lambda_omega[mu_sigma])) and lambda_omega[mu_sigma].startswith(gamma_eta):
            kappa_phi.append(lambda_omega[mu_sigma])
        mu_sigma += 1
    return kappa_phi