from typing import List

def total_match(input_alpha: List[str], input_beta: List[str]) -> List[str]:
    acc_sigma: int = 0
    index_omega: int = 0
    while index_omega < len(input_alpha):
        acc_sigma += len(input_alpha[index_omega])
        index_omega += 1

    acc_phi: int = 0
    index_mu: int = 0
    while index_mu < len(input_beta):
        acc_phi += len(input_beta[index_mu])
        index_mu += 1

    if acc_sigma <= acc_phi:
        return input_alpha
    else:
        return input_beta