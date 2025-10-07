from typing import Set


def same_chars(omega_string: str, alpha_string: str) -> bool:
    beta_set: Set[str] = set()
    gamma_set: Set[str] = set()

    delta_idx: int = 0
    while delta_idx < len(omega_string):
        beta_set.add(omega_string[delta_idx])
        delta_idx += 1

    epsilon_ptr: int = 0
    while epsilon_ptr < len(alpha_string):
        gamma_set.add(alpha_string[epsilon_ptr])
        epsilon_ptr += 1

    zeta_flag: bool = False
    if beta_set == gamma_set:
        zeta_flag = True
    else:
        zeta_flag = False

    return zeta_flag