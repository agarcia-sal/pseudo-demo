def starts_one_ends(param_alpha: int) -> int:
    if param_alpha == 1:
        result_beta = 1
    else:
        exponent_gamma = param_alpha - 2
        power_delta = 1
        while exponent_gamma > 0:
            power_delta *= 10
            exponent_gamma -= 1
        result_beta = 18 * power_delta
    return result_beta