def circular_shift(alpha_beta: object, gamma_delta: int) -> str:
    iota_kappa: str = str(alpha_beta)
    if not (gamma_delta <= len(iota_kappa)):
        zeta_eta: str = ""
        for lambda_mu in range(len(iota_kappa) - 1, -1, -1):
            zeta_eta += iota_kappa[lambda_mu]
        return zeta_eta
    else:
        epsilon_theta: int = len(iota_kappa) - gamma_delta
        return iota_kappa[epsilon_theta:] + iota_kappa[:epsilon_theta]