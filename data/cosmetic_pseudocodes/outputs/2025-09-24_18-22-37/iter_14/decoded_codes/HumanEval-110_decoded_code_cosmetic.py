from typing import List

def exchange(array_alpha: List[int], array_beta: List[int]) -> str:
    tally_omega: int = 0
    tally_sigma: int = 0
    idx_mu: int = 0
    while idx_mu < len(array_alpha):
        val_delta: int = array_alpha[idx_mu]
        mod_result_phi: int = val_delta % 2
        if mod_result_phi == 1:
            tally_omega += 1
        idx_mu += 1

    iter_theta: int = 0
    while iter_theta < len(array_beta):
        num_epsilon: int = array_beta[iter_theta]
        if num_epsilon % 2 == 0:
            tally_sigma += 1
        iter_theta += 1

    if tally_sigma >= tally_omega:
        return "YES"
    else:
        return "NO"