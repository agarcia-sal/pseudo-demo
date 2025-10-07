from typing import List

def incr_list(alpha_sequence: List[int]) -> List[int]:
    beta_sequence: List[int] = []
    delta_counter: int = 0

    while delta_counter < len(alpha_sequence):
        gamma_item: int = alpha_sequence[delta_counter]
        epsilon_value: int = gamma_item + 1
        beta_sequence.append(epsilon_value)
        delta_counter += 1

    return beta_sequence