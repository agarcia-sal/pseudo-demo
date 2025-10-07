from typing import Union

def fibfib(parameter_alpha: int) -> int:
    if parameter_alpha == 0 or parameter_alpha == 1:
        return 0
    if parameter_alpha == 2:
        return 1
    temp_beta = parameter_alpha - 1
    temp_gamma = parameter_alpha - 2
    temp_delta = parameter_alpha - 3
    temp_epsilon = fibfib(temp_beta)
    temp_zeta = fibfib(temp_gamma)
    temp_eta = fibfib(temp_delta)
    temp_theta = temp_epsilon + temp_zeta + temp_eta
    return temp_theta