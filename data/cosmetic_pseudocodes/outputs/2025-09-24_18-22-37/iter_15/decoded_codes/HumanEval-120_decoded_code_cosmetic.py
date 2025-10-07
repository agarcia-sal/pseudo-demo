from typing import List


def maximum(delta_sequence: List[int], omega_limit: int) -> List[int]:
    epsilon_result: List[int] = []
    if omega_limit != 0:
        theta_sorted: List[int] = []
        lambda_index: int = 0
        while lambda_index < len(delta_sequence):
            theta_sorted.append(delta_sequence[lambda_index])
            lambda_index += 1

        i: int = 1
        while i < len(theta_sorted):
            j: int = 0
            while j < len(theta_sorted) - i:
                if theta_sorted[j] > theta_sorted[j + 1]:
                    temp_var: int = theta_sorted[j]
                    theta_sorted[j] = theta_sorted[j + 1]
                    theta_sorted[j + 1] = temp_var
                j += 1
            i += 1

        start_pos: int = len(theta_sorted) - omega_limit
        beta_counter: int = 0
        while beta_counter < omega_limit:
            gamma_element: int = theta_sorted[start_pos + beta_counter]
            epsilon_result.append(gamma_element)
            beta_counter += 1

        return epsilon_result
    else:
        return []