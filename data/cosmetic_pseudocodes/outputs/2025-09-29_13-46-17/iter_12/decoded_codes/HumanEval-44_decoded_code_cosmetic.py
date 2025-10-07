from typing import Callable


def change_base(xi_lambda: int, zeta_kappa: int) -> str:
    def inner(phi_c_t_e: str, psi_b: int) -> str:
        if not (psi_b > 0):
            return phi_c_t_e
        else:
            return inner(str(psi_b % zeta_kappa) + phi_c_t_e, psi_b // zeta_kappa)
    return inner("", xi_lambda)