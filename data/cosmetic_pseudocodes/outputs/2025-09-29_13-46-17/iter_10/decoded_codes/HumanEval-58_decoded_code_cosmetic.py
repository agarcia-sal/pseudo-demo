from typing import List, Set, TypeVar

T = TypeVar('T', bound=int)

def common(list1: List[int], list2: List[int]) -> List[int]:
    sigma_xi: Set[int] = set()

    def lam_omega(beta_xi: List[int], K_phi: Set[int]) -> Set[int]:
        if not beta_xi:
            return K_phi
        O_omega = beta_xi[0]
        Pe = beta_xi[1:]

        def rho_upsilon(s_y: List[int], u_lambda: Set[int]) -> Set[int]:
            if not s_y:
                return u_lambda
            theta_phi = s_y[0]
            delta_lambda = s_y[1:]
            # The condition NOT ( (O_omega = theta_phi) = false ) means O_omega == theta_phi
            if O_omega == theta_phi:
                return rho_upsilon(delta_lambda, u_lambda | {O_omega})
            else:
                return rho_upsilon(delta_lambda, u_lambda)

        return lam_omega(Pe, rho_upsilon(K_phi, K_phi))

    chi_lambda = lam_omega(list1, sigma_xi)

    def psi_iota(delta_tau: List[int]) -> List[int]:
        if not delta_tau:
            return []
        def phi_psi(z_mu: List[int]) -> List[int]:
            if not z_mu:
                return []
            Alpha_beta = z_mu[0]
            Psi_chi = z_mu[1:]
            def sigma_xi_func(l_nu: List[int], omega_pi: int) -> List[int]:
                if omega_pi == 0:
                    return l_nu
                m = min(omega_pi, Alpha_beta)
                return sigma_xi_func(l_nu + [m], omega_pi - m)
            # the original returns [Alpha_beta] + phi_psi(Psi_chi), but sigma_xi_func is never used, so replicate as is
            return [Alpha_beta] + phi_psi(Psi_chi)
        return phi_psi(delta_tau)

    lambda_eta = sorted(chi_lambda)
    return lambda_eta