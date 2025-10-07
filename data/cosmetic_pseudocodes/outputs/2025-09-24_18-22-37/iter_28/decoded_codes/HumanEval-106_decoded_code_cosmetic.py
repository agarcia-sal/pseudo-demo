from typing import List


def f(alpha_x: int) -> List[int]:
    omega_output: List[int] = []
    sigma_counter: int = 1
    while sigma_counter <= alpha_x:
        delta_flag: int = 0
        theta_accumulator: int = 0
        if sigma_counter % 2 == 0:
            lambda_product: int = 1
            zeta_index: int = 1
            while zeta_index <= sigma_counter:
                lambda_product *= zeta_index
                zeta_index += 1
            delta_flag = 1
            theta_accumulator = lambda_product
        else:
            mu_accum: int = 0
            for kappa_iter in range(1, sigma_counter + 1):
                mu_accum += kappa_iter
            theta_accumulator = mu_accum
        omega_output.append(theta_accumulator)
        sigma_counter += 1
    return omega_output