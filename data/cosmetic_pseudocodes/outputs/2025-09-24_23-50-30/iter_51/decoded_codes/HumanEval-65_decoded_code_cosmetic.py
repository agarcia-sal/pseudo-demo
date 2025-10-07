from typing import Union

def circular_shift(parameter_alpha: Union[int, str], parameter_beta: int) -> str:
    beta_modulus: int = parameter_beta
    gamma_list: list[str] = list(str(parameter_alpha))
    delta_length: int = len(gamma_list)

    if not (delta_length < beta_modulus):
        return ''.join(reversed(gamma_list))
    else:
        epsilon_start: int = delta_length - beta_modulus
        zeta_end: int = delta_length
        eta_first: list[str] = gamma_list[epsilon_start:zeta_end]
        theta_second: list[str] = gamma_list[0:epsilon_start]
        return ''.join(eta_first + theta_second)