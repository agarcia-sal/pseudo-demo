from typing import Dict

def histogram(omega_input: str) -> Dict[str, int]:
    alpha_map: Dict[str, int] = {}
    beta_elements = omega_input.split(" ")
    gamma_peak = 0

    delta_idx = 0
    while delta_idx < len(beta_elements):
        epsilon_curr = beta_elements[delta_idx]
        if epsilon_curr != "":
            zeta_freq = 0
            eta_ptr = 0
            while eta_ptr < len(beta_elements):
                if beta_elements[eta_ptr] == epsilon_curr:
                    zeta_freq += 1
                eta_ptr += 1

            if zeta_freq > gamma_peak:
                gamma_peak = zeta_freq
        delta_idx += 1

    if gamma_peak <= 0:
        return alpha_map

    theta_index = 0
    while theta_index < len(beta_elements):
        iota_val = beta_elements[theta_index]
        if iota_val != "":
            kappa_count = 0
            for lambda_iter in range(len(beta_elements)):
                if beta_elements[lambda_iter] == iota_val:
                    kappa_count += 1

            if kappa_count == gamma_peak:
                alpha_map[iota_val] = gamma_peak
        theta_index += 1

    return alpha_map