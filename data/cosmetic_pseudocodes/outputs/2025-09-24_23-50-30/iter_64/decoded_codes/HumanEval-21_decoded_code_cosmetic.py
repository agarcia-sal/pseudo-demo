from typing import List

def rescale_to_unit(param_alpha: List[float]) -> List[float]:
    if not param_alpha:
        return []

    temp_gamma = param_alpha[0]
    temp_delta = param_alpha[0]
    idx_beta = 0
    while idx_beta < len(param_alpha):
        if param_alpha[idx_beta] < temp_gamma:
            temp_gamma = param_alpha[idx_beta]
        if param_alpha[idx_beta] > temp_delta:
            temp_delta = param_alpha[idx_beta]
        idx_beta += 1

    denom = temp_delta - temp_gamma
    idx_epsilon = 0
    result_zeta: List[float] = []
    while idx_epsilon < len(param_alpha):
        # Avoid division by zero if all values are equal
        if denom == 0:
            result_zeta.append(0.0)
        else:
            result_zeta.append((param_alpha[idx_epsilon] - temp_gamma) / denom)
        idx_epsilon += 1

    return result_zeta