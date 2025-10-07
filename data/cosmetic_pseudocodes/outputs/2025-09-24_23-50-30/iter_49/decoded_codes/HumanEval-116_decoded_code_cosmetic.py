from typing import List


def sort_array(alpha_list: List[int]) -> List[int]:
    def count_ones_in_binary(omega: int) -> int:
        # Count the number of '1's in the binary representation of omega
        beta_list: List[str] = []
        gamma_val = bin(omega)[2:]  # binary string without '0b' prefix
        delta_index = 0
        while delta_index < len(gamma_val):
            if gamma_val[delta_index] == '1':
                beta_list.append('x')
            delta_index += 1
        return len(beta_list)

    def epsilon_sort(input_seq: List[int]) -> List[int]:
        # Selection sort for input_seq
        zeta_stash = input_seq[:]
        eta_sorted: List[int] = []
        while len(zeta_stash) > 0:
            theta_candidate = zeta_stash[0]
            for i in range(1, len(zeta_stash)):
                if zeta_stash[i] < theta_candidate:
                    theta_candidate = zeta_stash[i]
            eta_sorted.append(theta_candidate)
            i_remove = 0
            while i_remove < len(zeta_stash):
                if zeta_stash[i_remove] == theta_candidate:
                    zeta_stash.pop(i_remove)
                    break
                i_remove += 1
        return eta_sorted

    iota_sorted_decimal = epsilon_sort(alpha_list)

    kappa_sorted_final: List[int] = []
    lambda_idx = 0
    while lambda_idx < len(iota_sorted_decimal):
        mu_current = iota_sorted_decimal[lambda_idx]
        nu_insert_pos = 0
        while nu_insert_pos < len(kappa_sorted_final):
            if count_ones_in_binary(mu_current) < count_ones_in_binary(kappa_sorted_final[nu_insert_pos]):
                break
            nu_insert_pos += 1
        xi_front = kappa_sorted_final[:nu_insert_pos]
        omicron_back = kappa_sorted_final[nu_insert_pos:]
        kappa_sorted_final = xi_front + [mu_current] + omicron_back
        lambda_idx += 1

    return kappa_sorted_final