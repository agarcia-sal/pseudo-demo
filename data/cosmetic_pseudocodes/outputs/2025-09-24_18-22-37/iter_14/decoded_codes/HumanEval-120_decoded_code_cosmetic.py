from typing import List

def maximum(delta_array: List[int], omega_count: int) -> List[int]:
    if omega_count != 0:
        sigma_list = delta_array[:]
        sigma_list.sort()
        beta_index = len(sigma_list) - omega_count
        gamma_sublist = sigma_list[beta_index:]
        return gamma_sublist
    else:
        return []