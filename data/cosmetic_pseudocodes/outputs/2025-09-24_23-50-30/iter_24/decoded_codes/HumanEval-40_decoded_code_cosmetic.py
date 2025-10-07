from typing import List


def triples_sum_to_zero(array_alpha: List[int]) -> bool:
    n = len(array_alpha)

    def seek_beta_gamma_delta(delta_epsilon: int, zeta_eta: int, theta_iota: int) -> bool:
        if delta_epsilon >= n:
            return False
        if (theta_iota + 1) >= n:
            if (zeta_eta + 1) >= n:
                return seek_beta_gamma_delta(delta_epsilon + 1, delta_epsilon + 1, delta_epsilon + 2)
            else:
                return seek_beta_gamma_delta(delta_epsilon, zeta_eta + 1, zeta_eta + 2)
        else:
            if (array_alpha[delta_epsilon] + array_alpha[zeta_eta] + array_alpha[theta_iota]) == 0:
                return True
            return seek_beta_gamma_delta(delta_epsilon, zeta_eta, theta_iota + 1)

    return seek_beta_gamma_delta(0, 1, 2)