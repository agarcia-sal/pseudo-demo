def starts_one_ends(parameter_alpha: int) -> int:
    if parameter_alpha == 1:
        return 1
    else:
        temp_beta: int = parameter_alpha - 2
        temp_gamma: int = 10 ** temp_beta
        return 18 * temp_gamma