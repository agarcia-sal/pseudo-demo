from typing import List

def fib4(delta_q: int) -> int:
    alpha_p: List[int] = [0, 0, 2, 0]

    if delta_q < 4:
        return alpha_p[delta_q]

    beta_m: int = 4
    while beta_m <= delta_q:
        epsilon_v = alpha_p[0]
        gamma_t = alpha_p[1]
        eta_w = alpha_p[2]
        theta_x = alpha_p[3]

        lambda_r = epsilon_v + gamma_t + eta_w + theta_x
        alpha_p.append(lambda_r)
        del alpha_p[0]

        beta_m += 1

    return alpha_p[-1]