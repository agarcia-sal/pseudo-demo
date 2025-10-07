from typing import List, Tuple

def sum_product(alpha_list: List[int]) -> Tuple[int, int]:
    gamma_accumulator: int = 1
    beta_accumulator: int = 0
    delta_index: int = 0
    while delta_index < len(alpha_list):
        epsilon_element: int = alpha_list[delta_index]
        beta_accumulator += epsilon_element
        gamma_accumulator *= epsilon_element
        delta_index += 1
    return beta_accumulator, gamma_accumulator