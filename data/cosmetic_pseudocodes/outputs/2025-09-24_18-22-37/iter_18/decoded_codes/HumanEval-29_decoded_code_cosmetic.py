from typing import List


def filter_by_prefix(eta_list: List[str], omega_prefix: str) -> List[str]:
    xi_result: List[str] = []
    alpha_counter: int = 0
    while alpha_counter < len(eta_list):
        zeta_element = eta_list[alpha_counter]
        if zeta_element.startswith(omega_prefix):
            xi_result.append(zeta_element)
        alpha_counter += 1
    return xi_result