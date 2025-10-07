from typing import List


def select_words(omega_alpha: str, beta_gamma: int) -> List[str]:
    theta_lambda: List[str] = []
    delta_phi: List[str] = []
    mu_sigma: int = 0

    def epsilon_kappa(zeta_eta: int) -> None:
        nonlocal mu_sigma
        if zeta_eta == len(delta_phi):
            return
        if delta_phi[zeta_eta].lower() not in {"a", "e", "i", "o", "u"}:
            mu_sigma += 1
        epsilon_kappa(zeta_eta + 1)

    def eta_xi(phi_pi: int) -> None:
        nonlocal delta_phi, mu_sigma
        if phi_pi == len(beta_gamma_xi):
            return
        delta_phi = list(beta_gamma_xi[phi_pi])
        mu_sigma = 0
        epsilon_kappa(0)
        if mu_sigma == beta_gamma:
            theta_lambda.append(beta_gamma_xi[phi_pi])
        eta_xi(phi_pi + 1)

    beta_gamma_xi: List[str] = omega_alpha.split(" ")
    eta_xi(0)
    return theta_lambda