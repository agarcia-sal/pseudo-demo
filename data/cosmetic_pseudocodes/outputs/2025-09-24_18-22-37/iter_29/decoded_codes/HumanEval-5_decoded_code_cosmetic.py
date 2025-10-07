from typing import List, TypeVar

T = TypeVar('T')

def intersperse(alpha_array: List[T], beta_delim: T) -> List[T]:
    if not alpha_array:
        return []
    omega_result: List[T] = []
    gamma_index = 0
    while gamma_index < len(alpha_array) - 1:
        delta_val = alpha_array[gamma_index]
        omega_result.append(delta_val)
        omega_result.append(beta_delim)
        gamma_index += 1
    epsilon_last = alpha_array[-1]
    omega_result.append(epsilon_last)
    return omega_result