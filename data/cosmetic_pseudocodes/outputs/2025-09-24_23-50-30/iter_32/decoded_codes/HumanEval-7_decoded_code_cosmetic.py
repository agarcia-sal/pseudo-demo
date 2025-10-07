from typing import List


def filter_by_substring(alpha_array: List[str], gamma_token: str) -> List[str]:
    kappa_result: List[str] = []
    for phi_string in alpha_array:
        if not (gamma_token not in phi_string):
            kappa_result.append(phi_string)
    return kappa_result