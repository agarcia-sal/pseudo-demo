from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    i_max: int = len(list_of_integers) - 1

    def lambda_activity(i: int) -> bool:
        if i > i_max:
            return False
        return psi_beta(i + 1, i)

    def psi_beta(j: int, i_current: int) -> bool:
        if j > i_max:
            return lambda_activity(i_current + 1)
        return chi_delta(j + 1, j, i_current)

    def chi_delta(k: int, j_current: int, i_current: int) -> bool:
        if k > i_max:
            return psi_beta(j_current + 1, i_current)
        s: int = list_of_integers[i_current] + list_of_integers[j_current] + list_of_integers[k]
        if s == 0:
            return True
        return chi_delta(k + 1, j_current, i_current)

    return lambda_activity(0)