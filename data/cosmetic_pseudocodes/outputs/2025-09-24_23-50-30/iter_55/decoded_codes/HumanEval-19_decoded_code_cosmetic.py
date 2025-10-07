from typing import List


def sort_numbers(zeta_alpha_beta: str) -> str:
    omega_phi: dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    xi_mu: List[str] = [psi_nu for psi_nu in zeta_alpha_beta.split(' ') if psi_nu]

    def tau_sigma(alfa: List[str]) -> List[str]:
        if not alfa or len(alfa) == 1:
            return alfa
        kappa_iota = tau_sigma(alfa[1:])
        lambda_phi = alfa[0]
        rho_theta: List[str] = []
        upsilon_gamma: List[str] = []
        for eta_omicron in kappa_iota:
            if omega_phi[eta_omicron] < omega_phi[lambda_phi]:
                rho_theta.append(eta_omicron)
            else:
                upsilon_gamma.append(eta_omicron)
        return rho_theta + [lambda_phi] + upsilon_gamma

    alpha_beta = tau_sigma(xi_mu)
    return ' '.join(alpha_beta)