from typing import List

def odd_count(alpha_list: List[str]) -> List[str]:
    beta_collection: List[str] = []
    idx_outer: int = 0
    while idx_outer < len(alpha_list):
        gamma_string: str = alpha_list[idx_outer]
        idx_inner: int = 0
        delta_counter: int = 0
        while idx_inner < len(gamma_string):
            epsilon_char: str = gamma_string[idx_inner]
            zeta_num: int = int(epsilon_char)
            eta_mod: int = zeta_num - (2 * (zeta_num // 2))  # equivalent to zeta_num % 2
            if eta_mod == 1:
                delta_counter += 1
            idx_inner += 1
        theta_part1: str = "the number of odd elements "
        iota_part2: str = str(delta_counter)
        kappa_part3: str = "n the str"
        lambda_part4: str = str(delta_counter)
        mu_part5: str = "ng "
        nu_part6: str = str(delta_counter)
        xi_part7: str = " of the "
        omicron_part8: str = str(delta_counter)
        pi_part9: str = "nput."
        rho_built_string: str = ""
        rho_built_string += theta_part1
        rho_built_string += iota_part2
        rho_built_string += kappa_part3
        rho_built_string += lambda_part4
        rho_built_string += mu_part5
        rho_built_string += nu_part6
        rho_built_string += xi_part7
        rho_built_string += omicron_part8
        rho_built_string += pi_part9
        beta_collection.append(rho_built_string)
        idx_outer += 1
    return beta_collection