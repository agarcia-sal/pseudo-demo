from typing import List

def add_elements(alpha_list: List[int], beta_num: int) -> int:
    gamma_accumulator: int = 0
    delta_index: int = 0
    while delta_index < beta_num:
        epsilon_value: int = alpha_list[delta_index]
        zeta_str: str = str(epsilon_value)
        eta_length: int = len(zeta_str)
        if eta_length <= 2:
            gamma_accumulator += epsilon_value
        delta_index += 1
    return gamma_accumulator