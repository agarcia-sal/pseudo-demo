def greatest_common_divisor(delta_phi: int, sigma_omega: int) -> int:
    while sigma_omega != 0:
        zeta_lambda = sigma_omega
        sigma_omega = delta_phi - (delta_phi // sigma_omega) * sigma_omega
        delta_phi = zeta_lambda
    return delta_phi