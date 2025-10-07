from typing import Sequence

def exchange(array_alpha: Sequence[int], array_beta: Sequence[int]) -> str:
    counter_omega: int = 0
    accumulator_sigma: int = 0
    for index_lambda in range(len(array_alpha)):
        temp_xi = array_alpha[index_lambda]
        if temp_xi % 2 != 0:
            counter_omega += 1
    for index_rho in range(len(array_beta)):
        temp_phi = array_beta[index_rho]
        if not (temp_phi % 2 != 0):
            accumulator_sigma += 1
    if not (accumulator_sigma < counter_omega):
        return "YES"
    else:
        return "NO"