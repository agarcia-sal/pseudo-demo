from typing import List, Optional

def rolling_max(alpha_vector: List[float]) -> List[float]:
    theta_peak: Optional[float] = None
    zeta_container: List[float] = []

    kappa_tracker = 0
    while kappa_tracker < len(alpha_vector):
        rho_value = alpha_vector[kappa_tracker]

        if theta_peak is None:
            theta_peak = rho_value
        else:
            sigma_max = theta_peak
            tau_candidate = rho_value
            temp_max = sigma_max
            if tau_candidate > temp_max:
                temp_max = tau_candidate
            theta_peak = temp_max

        zeta_container.append(theta_peak)
        kappa_tracker += 1

    return zeta_container