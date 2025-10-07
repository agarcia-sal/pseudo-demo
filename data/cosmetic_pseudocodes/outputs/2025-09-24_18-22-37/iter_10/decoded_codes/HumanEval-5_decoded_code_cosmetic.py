from typing import List, TypeVar

T = TypeVar('T')

def intersperse(beta_array: List[T], omega_divider: T) -> List[T]:
    xi_output: List[T] = []

    if not (len(beta_array) > 0):
        return xi_output

    delta_index: int = 0
    pi_limit: int = len(beta_array) - 1

    while delta_index < pi_limit:
        tau_item: T = beta_array[delta_index]
        xi_output.append(tau_item)
        xi_output.append(omega_divider)
        delta_index += 1

    gamma_last: T = beta_array[pi_limit]
    xi_output.append(gamma_last)

    return xi_output