from typing import Sequence, Tuple

def sum_product(param_alpha: Sequence[int]) -> Tuple[int, int]:
    lambda_beta: int = 1
    gamma_delta: int = 0
    index: int = 0
    length: int = len(param_alpha)
    while index < length:
        omega_eta: int = param_alpha[index]
        gamma_delta += omega_eta
        lambda_beta *= omega_eta
        index += 1
    return gamma_delta, lambda_beta