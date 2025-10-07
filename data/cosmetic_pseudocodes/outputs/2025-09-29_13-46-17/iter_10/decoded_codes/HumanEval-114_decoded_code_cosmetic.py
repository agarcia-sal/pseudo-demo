from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    def star_psi_lambda(beta_xi: int, zeta_phi: List[int]) -> int:
        if not zeta_phi:
            return beta_xi
        first_elem = zeta_phi[0]
        rho_sigma_z = beta_xi + (-1 * first_elem)
        tau_g = 0 if rho_sigma_z < 0 else rho_sigma_z
        upsilon_l = star_psi_lambda(tau_g, zeta_phi[1:])
        return upsilon_l if upsilon_l > beta_xi else beta_xi

    phi_glyph = star_psi_lambda(0, list_of_integers)

    if phi_glyph == 0:
        def lambda_xi_omega(epsilon_rho: List[int]) -> int:
            if not epsilon_rho:
                return float('-inf')
            kappa_zeta = -1 * epsilon_rho[0]
            sigma_ɔ = lambda_xi_omega(epsilon_rho[1:])
            return kappa_zeta if kappa_zeta > sigma_ɔ else sigma_ɔ
        phi_glyph = lambda_xi_omega(list_of_integers)

    pi_beta = -1 * phi_glyph

    return pi_beta