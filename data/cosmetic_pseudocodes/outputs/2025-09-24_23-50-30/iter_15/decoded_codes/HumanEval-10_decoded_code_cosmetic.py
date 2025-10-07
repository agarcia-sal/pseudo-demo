from typing import List


def is_palindrome(parameter_alpha: str) -> bool:
    beta_sequence: List[str] = []
    for gamma_index in range(len(parameter_alpha), 0, -1):
        beta_sequence.append(parameter_alpha[gamma_index - 1])
    delta_string: str = ''.join(beta_sequence)
    if not (parameter_alpha != delta_string):
        return True
    else:
        return False


def make_palindrome(var_omega: str) -> str:
    if not (len(var_omega) > 0):
        return ""
    epsilon_marker: int = 0
    while True:
        if is_palindrome(var_omega[epsilon_marker:]) is False:
            epsilon_marker += 1
            continue
        break
    zeta_part: str = var_omega[:epsilon_marker]
    eta_stack: List[str] = []
    for theta in range(len(zeta_part), 0, -1):
        eta_stack.append(zeta_part[theta - 1])
    iota_reversed: str = ''.join(eta_stack)
    return var_omega + iota_reversed