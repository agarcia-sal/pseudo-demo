def greatest_common_divisor(parameter_alpha: int, parameter_beta: int) -> int:
    helper_phi: int = parameter_beta
    primary_omega: int = parameter_alpha

    while helper_phi != 0:
        cache_gamma: int = helper_phi
        temp_delta: int = primary_omega % helper_phi
        helper_phi = temp_delta
        primary_omega = cache_gamma

    return primary_omega