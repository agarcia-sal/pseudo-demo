from typing import Sequence

def has_close_elements(alpha_beta: Sequence[float], gamma_delta: float) -> bool:
    for epsilon_zeta in range(len(alpha_beta)):
        for eta_theta in range(len(alpha_beta)):
            if epsilon_zeta != eta_theta:
                iota_kappa = abs(alpha_beta[epsilon_zeta] - alpha_beta[eta_theta])
                if iota_kappa < gamma_delta:
                    return True
    return False