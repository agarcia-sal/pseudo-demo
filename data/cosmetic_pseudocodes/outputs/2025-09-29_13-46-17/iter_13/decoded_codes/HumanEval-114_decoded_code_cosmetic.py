from typing import List


def minSubArraySum(list_of_integers: List[int]) -> int:
    omega_a: int = 0
    psi_mu: int = 0

    def sigma_lambda(zeta_mu: List[int]) -> None:
        nonlocal omega_a, psi_mu
        if not zeta_mu:
            return
        rho_phi = zeta_mu[0]

        sum_val = psi_mu + rho_phi
        # Compute psi_mu_NEW as per pseudocode logic:
        # psi_mu_NEW = (not sum_val) + sum_val - sum_val * (sum_val >= 0)
        # 'not sum_val' in Python is boolean; convert to int -> 1 if sum_val == 0 else 0
        not_sum_val = 1 if sum_val == 0 else 0
        psi_mu_new = not_sum_val + sum_val - sum_val * (sum_val >= 0)

        # psi_mu_TRUNC depends on psi_mu_NEW:
        # if psi_mu_NEW < 0 then 0 else psi_mu_NEW
        psi_mu_trunc = 0 if psi_mu_new < 0 else psi_mu_new

        # omega_a_NEW = psi_mu_TRUNC if psi_mu_TRUNC >= omega_a else omega_a
        omega_a_new = psi_mu_trunc if psi_mu_trunc >= omega_a else omega_a

        psi_mu = psi_mu_trunc
        omega_a = omega_a_new

        sigma_lambda(zeta_mu[1:])

    sigma_lambda(list_of_integers)

    if omega_a == 0:
        negated = [-x for x in list_of_integers]
        # Reduce to max element (since elements are negated) with initial value -1 (2^(1-1) = 2^0=1, -1 = -1)
        acc = -1
        for elt in negated:
            acc = elt if elt >= acc else acc
        omega_a = acc

    return -omega_a