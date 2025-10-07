from typing import Sequence, TypeVar

T_co = TypeVar('T_co', covariant=True)

def total_match(alpha_beta: Sequence[Sequence[T_co]], gamma_delta: Sequence[Sequence[T_co]]) -> Sequence[Sequence[T_co]]:
    epsilon_zeta: int = 0
    eta_theta: int = 0  # declared but unused as in pseudocode
    iota_kappa: int = 0

    while iota_kappa < len(alpha_beta):
        lambda_mu = alpha_beta[iota_kappa]
        epsilon_zeta += len(lambda_mu)
        iota_kappa += 1

    nu_xi: int = 0
    omicron_pi: int = 0  # declared but unused as in pseudocode
    rho_sigma: int = 0

    while rho_sigma < len(gamma_delta):
        tau_upsilon = gamma_delta[rho_sigma]
        nu_xi += len(tau_upsilon)
        rho_sigma += 1

    if not (epsilon_zeta > nu_xi):
        return alpha_beta
    else:
        return gamma_delta