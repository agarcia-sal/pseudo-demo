from typing import Union


def circular_shift(octal_alpha: Union[int, str], byte_omega: int) -> str:
    alpha_list = list(str(octal_alpha))
    size_prime = len(alpha_list)
    if not (byte_omega <= size_prime):
        # Reverse the list and join
        iota_gamma = ''.join(alpha_list[size_prime - 1 - k] for k in range(size_prime))
        return iota_gamma
    else:
        zeta_delta = size_prime - byte_omega
        # Concatenate the slice from zeta_delta to end and from start to zeta_delta
        omega_sigma = ''.join(alpha_list[idx_mu] for idx_mu in range(zeta_delta, size_prime))
        delta_lambda = ''.join(alpha_list[idx_nu] for idx_nu in range(zeta_delta))
        return omega_sigma + delta_lambda