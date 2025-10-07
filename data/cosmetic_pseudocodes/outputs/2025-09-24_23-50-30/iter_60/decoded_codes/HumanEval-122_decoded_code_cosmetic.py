from typing import List


def add_elements(beta_list: List[int], gamma_num: int) -> int:
    def zeta_recursive(theta_index: int, iota_accum: int) -> int:
        if theta_index > gamma_num:
            return iota_accum
        # Check if the string length of beta_list[theta_index] is NOT greater than 2
        if not (len(str(beta_list[theta_index])) > 2):
            return zeta_recursive(theta_index + 1, iota_accum + beta_list[theta_index])
        else:
            return zeta_recursive(theta_index + 1, iota_accum)

    return zeta_recursive(1, 0)