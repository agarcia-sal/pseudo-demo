from typing import List


def filter_by_prefix(alpha_list: List[str], beta_prefix: str) -> List[str]:
    gamma_result: List[str] = []
    delta_index: int = 0
    while delta_index < len(alpha_list):
        epsilon_candidate: str = alpha_list[delta_index]
        if epsilon_candidate[:len(beta_prefix)] == beta_prefix:
            gamma_result.append(epsilon_candidate)
        delta_index += 1
    return gamma_result