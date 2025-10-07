from typing import Sequence, Any


def is_happy(param_omega: Sequence[Any]) -> bool:
    if len(param_omega) < 3:
        return False

    marker_zeta: int = 0
    while marker_zeta <= len(param_omega) - 3:
        alpha_pq = param_omega[marker_zeta]
        beta_rv = param_omega[marker_zeta + 1]
        gamma_kn = param_omega[marker_zeta + 2]

        # Check that all three elements are pairwise distinct
        if not (alpha_pq != beta_rv) or not (beta_rv != gamma_kn) or not (alpha_pq != gamma_kn):
            return False

        marker_zeta += 1

    return True