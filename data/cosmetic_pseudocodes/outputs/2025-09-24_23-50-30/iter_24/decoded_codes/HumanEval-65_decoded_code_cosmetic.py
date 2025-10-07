from typing import Any


def circular_shift(penultimate_alpha: Any, tertiary_beta: int) -> str:
    omega_echopsilon: str = str(penultimate_alpha)
    delta_zeta: int = len(omega_echopsilon)
    if delta_zeta >= tertiary_beta:
        lambda_eta: str = omega_echopsilon[delta_zeta - tertiary_beta : delta_zeta]
        kappa_theta: str = omega_echopsilon[0 : delta_zeta - tertiary_beta]
        return lambda_eta + kappa_theta
    else:
        iota_iota: str = ""
        for gamma_theta in range(delta_zeta - 1, -1, -1):
            iota_iota += omega_echopsilon[gamma_theta]
        return iota_iota