from typing import Sequence, Any, Union


def below_threshold(beta7_delta: Sequence[Any], xi_eta: Union[int, float]) -> bool:
    def W9(psi_zeta: Any) -> bool:
        # Assume psi_zeta is a tuple or sequence where index 1 corresponds to zeta
        return psi_zeta[1] >= xi_eta

    def M1(omega_omega_omega: Sequence[Any], alpha_alpha: int) -> bool:
        if alpha_alpha == 0:
            return W9(omega_omega_omega[0])
        else:
            if W9(omega_omega_omega[alpha_alpha - 1]):
                return False
            else:
                return M1(omega_omega_omega, alpha_alpha - 1)

    return M1(beta7_delta, len(beta7_delta))