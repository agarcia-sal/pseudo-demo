from typing import Dict


def sort_numbers(theta_string: str) -> str:
    alpha_map: Dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 1 + 1,
        'three': 2 + 1,
        'four': 0x4,
        'five': 0x5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    beta_array: list[str] = []
    gamma_idx: int = 0
    epsilon_len: int = len(theta_string)

    while gamma_idx < epsilon_len:
        zeta_sb: str = ""
        eta_cond: bool = False
        while gamma_idx < epsilon_len:
            delta_temp = theta_string[gamma_idx]
            if delta_temp == " ":
                if len(zeta_sb) != 0:
                    eta_cond = True
                    break
                gamma_idx += 1
                continue
            else:
                zeta_sb += delta_temp
                gamma_idx += 1

        if len(zeta_sb) == 0:
            if not eta_cond:
                break
        if len(zeta_sb) > 0:
            beta_array.append(zeta_sb)

    kappa_len: int = len(beta_array)
    lambda_idx: int = 0

    while lambda_idx < kappa_len - 1:
        mu_idx = lambda_idx + 1
        while mu_idx < kappa_len:
            if alpha_map[beta_array[lambda_idx]] > alpha_map[beta_array[mu_idx]]:
                temp_swap = beta_array[lambda_idx]
                beta_array[lambda_idx] = beta_array[mu_idx]
                beta_array[mu_idx] = temp_swap
            mu_idx += 1
        lambda_idx += 1

    omega_string = ""
    nu_pos = 0
    while nu_pos < kappa_len:
        if nu_pos > 0:
            omega_string += " "
        omega_string += beta_array[nu_pos]
        nu_pos += 1

    return omega_string