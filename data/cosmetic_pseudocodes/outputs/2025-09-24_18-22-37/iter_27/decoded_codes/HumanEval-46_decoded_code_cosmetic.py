from typing import List


def fib4(delta_q: int) -> int:
    beta_r: List[int] = [0, 0, 2, 0]
    if delta_q < 4:
        return beta_r[delta_q]

    zeta_s: int = 4
    while zeta_s <= delta_q:
        chi_t = beta_r[0]
        omega_u = beta_r[1]
        alpha_v = beta_r[2]
        gamma_w = beta_r[3]
        kappa_x = chi_t + omega_u
        lambda_y = kappa_x + alpha_v
        next_value = lambda_y + gamma_w

        beta_r.append(next_value)
        beta_r.pop(0)  # remove the first element to shift window
        zeta_s += 1

    result_z = beta_r[-1]
    return result_z