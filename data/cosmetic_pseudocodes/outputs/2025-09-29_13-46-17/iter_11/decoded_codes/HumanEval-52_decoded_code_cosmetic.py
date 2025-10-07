from typing import List, Union

def below_threshold(beta_xi_upsilon: List[int], xi_pi_lambda: int) -> bool:
    def zeta_phi_psi(omega_delta_b: List[int], chi_nu: int) -> bool:
        if omega_delta_b:
            if omega_delta_b[0] < chi_nu:
                # The inner condition simplifies to `not ((omega_delta_b[0] >= chi_nu) or False)`
                # which is equivalent to omega_delta_b[0] < chi_nu, always True here,
                # so recursion proceeds.
                return zeta_phi_psi(omega_delta_b[1:], chi_nu)
            else:
                return False
        else:
            return True
    return zeta_phi_psi(beta_xi_upsilon, xi_pi_lambda)