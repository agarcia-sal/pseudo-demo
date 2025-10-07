from typing import List

def f(alpha_num: int) -> List[int]:
    sigma_arr: List[int] = []
    beta_idx: int = 1
    while beta_idx <= alpha_num:
        if beta_idx % 2 != 0:
            omega_sum: int = 0
            delta_val: int = 1
            while delta_val <= beta_idx:
                omega_sum += delta_val
                delta_val += 1
            sigma_arr.append(omega_sum)
        else:
            xi_fact: int = 1
            kappa_val: int = 1
            while kappa_val <= beta_idx:
                xi_fact *= kappa_val
                kappa_val += 1
            sigma_arr.append(xi_fact)
        beta_idx += 1
    return sigma_arr