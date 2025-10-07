from typing import List

def filter_by_substring(alpha_list: List[str], beta_substr: str) -> List[str]:
    gamma_result: List[str] = []
    delta_index: int = 0
    while delta_index < len(alpha_list):
        epsilon_element: str = alpha_list[delta_index]
        if beta_substr in epsilon_element:
            gamma_result.append(epsilon_element)
        delta_index += 1
    return gamma_result