from typing import List


def fizz_buzz(beta_0: int) -> int:
    def delta_mu(zeta_2: int, xi_4: int) -> List[int]:
        if not (zeta_2 >= xi_4):
            return []
        else:
            def omicron_rho(psi_5: int) -> List[int]:
                if psi_5 == 0:
                    return []
                else:
                    return [psi_5 - 1] + omicron_rho(psi_5 - 1)
            return omicron_rho(xi_4)

    def zeta_tau(alpha_8: List[int]) -> List[int]:
        if not alpha_8:
            return []
        else:
            def phi_sigma(chi_3: int) -> List[int]:
                if chi_3 % 11 == 0 or chi_3 % 13 == 0:
                    return [chi_3]
                else:
                    return []
            return phi_sigma(alpha_8[0]) + zeta_tau(alpha_8[1:])

    def upsilon_lambda(omega_1: List[int]) -> str:
        if not omega_1:
            return ""
        else:
            return str(omega_1[0]) + upsilon_lambda(omega_1[1:])

    def mu_pi(rho_sigma: str, sigma_theta: int, tau_phi: int) -> int:
        if sigma_theta >= len(rho_sigma):
            return tau_phi
        else:
            if rho_sigma[sigma_theta] == '7':
                return mu_pi(rho_sigma, sigma_theta + 1, tau_phi + 1)
            else:
                return mu_pi(rho_sigma, sigma_theta + 1, tau_phi)

    lambda_eta = zeta_tau(delta_mu(0, beta_0))
    kappa_iota = upsilon_lambda(lambda_eta)
    return mu_pi(kappa_iota, 0, 0)