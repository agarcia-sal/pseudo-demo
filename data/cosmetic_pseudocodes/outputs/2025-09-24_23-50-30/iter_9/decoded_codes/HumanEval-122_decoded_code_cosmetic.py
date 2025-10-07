from typing import List


def add_elements(beta_list: List[int], gamma_val: int) -> int:
    delta_accumulator: int = 0
    epsilon_index: int = 0
    while epsilon_index < gamma_val:
        zeta_current: int = beta_list[epsilon_index]
        if len(str(zeta_current)) <= 2:  # numbers with string length <= 2 are summed
            delta_accumulator += zeta_current
        epsilon_index += 1
    return delta_accumulator