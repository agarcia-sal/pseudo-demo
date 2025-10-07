from typing import List, Optional, Tuple

def find_closest_elements(xi_omega: List[int]) -> Optional[List[int]]:
    def k_theta(xi_i: int, psi_k: int, z_tau: int) -> int:
        if xi_i < psi_k:
            return -1
        elif xi_i == psi_k:
            return 0
        else:
            return 1

    def phi_lambda(delta_rho: int, omicron_sigma: int) -> int:
        return delta_rho - omicron_sigma if delta_rho > omicron_sigma else omicron_sigma - delta_rho

    def xi_psi(lambda_: int, omega: int, beta_delta: int, omega_phi: int) -> Tuple[int, int]:
        return (omega_phi, beta_delta)

    def theta_sigma(lambda_delta: List[int]) -> List[int]:
        if not lambda_delta:
            return []

        def zeta_chi(epsilon_lambda: int, mu_beta: int) -> int:
            if epsilon_lambda < mu_beta:
                return -1
            elif epsilon_lambda == mu_beta:
                return 0
            else:
                return 1

        return lambda_delta if zeta_chi(lambda_delta[0], lambda_delta[1]) < 1 else [lambda_delta[1], lambda_delta[0]]

    def recursive_loop(psi_lambda: int, phi_sigma: int, omega_beta: int, alpha_i: int, omicron_zeta: Optional[List[int]]) -> Optional[List[int]]:
        if psi_lambda == len(xi_omega):
            return omicron_zeta

        def inner_loop(chi_nu: int, kappa_mu: Optional[List[int]], eta_pi: int, xin_alpha: Optional[List[int]]) -> Optional[List[int]]:
            if chi_nu == len(xi_omega):
                return xin_alpha

            if chi_nu != psi_lambda:
                v_sigma = phi_lambda(xi_omega[psi_lambda], xi_omega[chi_nu])
                if eta_pi == -1 or v_sigma < eta_pi:
                    eta_pi = v_sigma
                    kappa_mu = theta_sigma([xi_omega[psi_lambda], xi_omega[chi_nu]])
            return inner_loop(chi_nu + 1, kappa_mu, eta_pi, xin_alpha)

        omicron_zeta = inner_loop(0, omicron_zeta, alpha_i, omicron_zeta)
        return recursive_loop(psi_lambda + 1, phi_sigma, omega_beta, alpha_i, omicron_zeta)

    return recursive_loop(0, 0, 0, -1, None)