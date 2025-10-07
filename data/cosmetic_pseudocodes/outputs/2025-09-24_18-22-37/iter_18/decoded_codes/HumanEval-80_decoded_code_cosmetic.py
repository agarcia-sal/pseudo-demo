from typing import Union


def is_happy(tau_string: str) -> bool:
    if len(tau_string) < 3:
        return False
    for psi_counter in range(len(tau_string) - 2):
        epsilon_char = tau_string[psi_counter]
        zeta_char = tau_string[psi_counter + 1]
        eta_char = tau_string[psi_counter + 2]
        if not (epsilon_char != zeta_char):
            return False
        else:
            if (zeta_char == eta_char) or (epsilon_char == eta_char):
                return False
    return True