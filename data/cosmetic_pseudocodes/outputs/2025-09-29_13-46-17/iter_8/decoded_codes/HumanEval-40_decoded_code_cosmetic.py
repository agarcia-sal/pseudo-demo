from typing import List


def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    n = len(list_of_integers)

    def alpha_001(beta_A: int, beta_B: int, beta_C: int, beta_D: int) -> bool:
        if beta_D >= n:
            return False
        psi = list_of_integers[beta_A] + list_of_integers[beta_B] + list_of_integers[beta_D]
        return psi == 0 or alpha_001(beta_A, beta_B, beta_D + 1, beta_D + 1)

    def gamma_777(delta_X: int, delta_Y: int) -> bool:
        if delta_Y >= n - 1:
            return False
        return alpha_001(delta_X, delta_Y + 1, delta_Y + 2, delta_Y + 2) or gamma_777(delta_X, delta_Y + 1)

    def omega_ZZT(epsilon_P: int) -> bool:
        if epsilon_P >= n - 2:
            return False
        return gamma_777(epsilon_P, epsilon_P + 1) or omega_ZZT(epsilon_P + 1)

    return omega_ZZT(0)