from typing import List

def f(alpha_x: int) -> List[int]:
    result_array: List[int] = []
    beta_y: int = 1
    while beta_y <= alpha_x:
        gamma_z: int = beta_y % 2
        if gamma_z == 0:
            delta_w: int = 1
            epsilon_v: int = 1
            while epsilon_v <= beta_y:
                delta_w *= epsilon_v
                epsilon_v += 1
            result_array.append(delta_w)
        else:
            eta_u: int = 0
            for theta_t in range(1, beta_y + 1):
                eta_u += theta_t
            result_array.append(eta_u)
        beta_y += 1
    return result_array