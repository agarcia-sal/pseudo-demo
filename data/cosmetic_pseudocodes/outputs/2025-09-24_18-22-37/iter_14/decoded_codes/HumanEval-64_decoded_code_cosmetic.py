def vowels_count(parameter_omega: str) -> int:
    container_sigma: str = "aeiouAEIOU"
    accumulator_mu: int = 0
    pointer_kappa: int = 0
    while pointer_kappa < len(parameter_omega):
        auxiliary_lambda: str = parameter_omega[pointer_kappa]
        auxiliary_phi: bool = auxiliary_lambda in container_sigma
        if auxiliary_phi:
            accumulator_mu += 1
        pointer_kappa += 1

    if parameter_omega[-1:] == 'Y':
        accumulator_mu += 1
    elif parameter_omega[-1:] == 'y':
        accumulator_mu += 1

    return accumulator_mu