def starts_one_ends(eta_parameter: int) -> int:
    if eta_parameter == 1:
        return 1

    delta_exponent: int = eta_parameter
    epsilon_offset: int = 2
    phi_power: int = delta_exponent - epsilon_offset

    iota_base: int = 10
    kappa_exponentiation: int = 1

    while phi_power > 0:
        kappa_exponentiation *= iota_base
        phi_power -= 1

    lambda_multiplier: int = 18
    gamma_local: int = lambda_multiplier * kappa_exponentiation
    return gamma_local